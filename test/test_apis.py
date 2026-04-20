"""
# https://docs.astral.sh/uv/getting-started/installation/
# https://gitee.com/wangnov/uv-custom/releases
uv venv
uv pip sync /dev/null --allow-empty-requirements
# uv pip sync NUL --allow-empty-requirements
uv pip install aiohttp
uv pip freeze > ./requirements.txt
uv run ./test_apis.py
"""
# 第三方库
import aiohttp

# 标准库
import os
import sys
import time
import json
import shutil
import asyncio
import argparse
from pathlib import Path

# 测试用的IP地址
TEST_IPS = [
    "117.30.120.138", # 中国 福建厦门集美
    "1.1.1.1",        # 澳大利亚
    "8.8.8.8",        # 美国
]

# 所有API列表 (从README中提取)
# 格式: (名称, URL模板, 请求类型, 是否支持查询指定IP, 备注)
APIS = [
    # === 1. 可查询本机IP和通过IP查询信息 ===
    ("ip-api.com", "http://ip-api.com/json/{ip}?lang=zh-CN", "GET", True, "支持中文"),
    ("demo.ip-api.com", "http://demo.ip-api.com/json/{ip}?fields=66842623&lang=zh-CN", "GET", True, "支持中文"),
    ("pconline", "https://whois.pconline.com.cn/ipJson.jsp?ip={ip}&json=true", "GET", True, "返回GBK编码"),
    ("ip.sb", "https://api.ip.sb/geoip/{ip}", "GET", True, ""),
    ("ip2location.io", "https://api.ip2location.io/?ip={ip}", "GET", True, "免费5000次/天"),
    ("realip.cc", "https://realip.cc/?ip={ip}", "GET", True, ""),
    ("ipapi.co", "https://ipapi.co/{ip}/json/", "GET", True, "支持CORS"),
    ("ipapi.is", "https://api.ipapi.is/?ip={ip}", "GET", True, ""),
    ("db-ip.com", "https://api.db-ip.com/v2/free/{ip}", "GET", True, ""),
    ("freeipapi.com", "https://freeipapi.com/api/json/{ip}", "GET", True, ""),
    ("ipwhois.app", "https://ipwhois.app/json/{ip}?format=json", "GET", True, ""),
    ("ip.nc.gy", "https://ip.nc.gy/json?ip={ip}", "GET", True, ""),
    ("geojs.io", "https://get.geojs.io/v1/ip/geo/{ip}.json", "GET", True, ""),
    ("baidu.opendata", "https://opendata.baidu.com/api.php?co=&resource_id=6006&oe=utf8&query={ip}", "GET", True, ""),
    
    # === 2. 只可查询本机IP ===
    ("httpbin.org", "http://httpbin.org/ip", "GET", False, ""),
    ("cdid.ctrip", "https://cdid.c-ctrip.com/model-poc2/h", "GET", False, ""),
    ("qq.video", "https://vv.video.qq.com/checktime?otype=ojson", "GET", False, ""),
    ("test.ipw.cn", "https://test.ipw.cn/api/ip/myip?json", "GET", False, ""),
    ("api.ipify.org", "https://api.ipify.org?format=json", "GET", False, ""),
    ("my.ipinfo.app", "https://ipv4.my.ipinfo.app/api/ipDetails.php", "GET", False, ""),
    ("g3.letv", "https://g3.letv.com/r?format=1", "GET", False, ""),
    ("qq.inews", "https://r.inews.qq.com/api/ip2city", "GET", False, ""),
    ("myip.ipip.net", "https://myip.ipip.net/json", "GET", False, ""),
    ("ifconfig.me", "https://ifconfig.me/all.json", "GET", False, ""),
    ("geolocation-db.com", "https://geolocation-db.com/json", "GET", False, ""),
    ("api.myip.com", "https://api.myip.com", "GET", False, ""),
    ("wtfismyip.com", "https://wtfismyip.com/json", "GET", False, ""),
    ("ipbase.com", "https://api.ipbase.com/v1/json", "GET", False, ""),
    ("ipquery.io", "https://api.ipquery.io/?format=json", "GET", False, ""),
    ("cloudflare.trace", "https://1.1.1.1/cdn-cgi/trace", "GET", False, ""),
    ("torproject", "https://check.torproject.org/api/ip", "GET", False, ""),
    ("bilibili", "https://api.live.bilibili.com/xlive/web-room/v1/index/getIpInfo", "GET", False, ""),
    ("news.qq", "https://i.news.qq.com/api/ip2city", "GET", False, ""),
    ("gdt.qq", "https://ipv4.gdt.qq.com/get_client_ip", "GET", False, "返回纯文本"),
    ("cip.cc", "http://www.cip.cc/{ip}", "GET", True, "返回文本格式"),
    
    # === 3. 只可通过IP查询 ===
    ("ipinfo.io", "https://ipinfo.io/widget/demo/{ip}", "GET", True, ""),
    ("db-ip.demo", "https://db-ip.com/demo/home.php?s={ip}", "GET", True, ""),
    ("iqiyi.mesh", "https://mesh.if.iqiyi.com/aid/ip/info?ip={ip}", "GET", True, ""),
]

# 已失效的API (也包含在测试中，方便手动验证)
DEPRECATED_APIS = [
    ("meitu.webapi", "https://webapi-pc.meitu.com/common/ip_location?ip={ip}", "GET", True, "已失效"),
    ("ip.cn", "https://www.ip.cn/api/index?ip={ip}&type=0", "GET", True, "已失效"),
    ("vore.top", "https://api.vore.top/api/IPdata?ip={ip}", "GET", True, "已失效"),
    ("qjqq.cn", "https://api.qjqq.cn/api/Local?ip={ip}", "GET", True, "已失效"),
    ("csdn.searchplugin", "https://searchplugin.csdn.net/api/v1/ip/get?ip={ip}", "GET", True, "已失效"),
    ("ip-api.io", "https://ip-api.io/json?ip={ip}", "GET", True, "已失效"),
    ("useragentinfo", "https://ip.useragentinfo.com/json", "GET", False, "已失效"),
    ("uomg.com", "https://api.uomg.com/api/visitor.info?skey=1", "GET", False, "已失效"),
    ("baidu.qifu", "https://qifu-api.baidubce.com/ip/local/geo/v1/district", "GET", False, "已失效"),
    ("ipapi.com", "https://ipapi.com/ip_api.php?ip={ip}", "GET", True, "已失效"),
]


async def test_api(session, name, url_template, req_type, supports_ip, remark, test_ip):
    """测试单个API"""
    start_time = time.time()
    status = "unknown"
    result = None
    error = None
    
    # 构造URL
    if supports_ip:
        url = url_template.format(ip=test_ip)
    else:
        url = url_template
    
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as resp:
            elapsed = time.time() - start_time
            content_type = resp.headers.get("Content-Type", "")
            
            try:
                if "json" in content_type or "javascript" in content_type:
                    result = await resp.json()
                else:
                    text = await resp.text()
                    result = {"raw": text[:500]}  # 截取前500字符
                
                status = "success" if resp.status == 200 else f"http_{resp.status}"
            except Exception as e:
                error = f"parse_error: {str(e)[:100]}"
                status = "parse_error"
                
    except asyncio.TimeoutError:
        status = "timeout"
        error = "请求超时"
    except aiohttp.ClientError as e:
        status = "error"
        error = str(e)[:100]
    except Exception as e:
        status = "error"
        error = str(e)[:100]
    
    elapsed = time.time() - start_time
    
    return {
        "name": name,
        "url": url,
        "status": status,
        "elapsed_ms": round(elapsed * 1000, 2),
        "remark": remark,
        "supports_ip": supports_ip,
        "result": result,
        "error": error
    }


async def run_tests(concurrency, include_deprecated, verbose, clear):
    """运行所有测试"""
    all_apis = list(APIS)
    if include_deprecated:
        all_apis.extend(DEPRECATED_APIS)
    
    print(f"测试 {len(all_apis)} 个API，并发数: {concurrency}")
    print("=" * 80)
    
    # 创建输出目录
    output_dir = Path(__file__).parent.parent / "output"
    output_dir.mkdir(exist_ok=True)
    
    # 清空output目录（JSON文件）
    if clear:
        for item in output_dir.iterdir():
            if item.is_file() and item.suffix == ".json":
                item.unlink()
        print("已清空旧的JSON文件")
    
    # verbose模式：按API站点分组
    verbose_dir = output_dir / "by_api" if verbose else None
    if verbose_dir:
        verbose_dir.mkdir(exist_ok=True)
        # 清空旧数据
        for item in verbose_dir.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
    
    results = []
    semaphore = asyncio.Semaphore(concurrency)
    
    async with aiohttp.ClientSession() as session:
        # 为每个IP测试所有API
        for test_ip in TEST_IPS:
            print(f"\n>>> 测试IP: {test_ip}")
            print("-" * 60)
            
            tasks = []
            for api in all_apis:
                name, url_template, req_type, supports_ip, remark = api
                
                async def bounded_test(api_tuple):
                    async with semaphore:
                        return await test_api(session, *api_tuple, test_ip)
                
                tasks.append(bounded_test(api))
            
            # 并发执行
            batch_results = await asyncio.gather(*tasks)
            
            for r in batch_results:
                r["test_ip"] = test_ip
                results.append(r)
                
                # verbose模式：保存到对应API文件夹
                if verbose_dir:
                    api_dir = verbose_dir / r["name"]
                    api_dir.mkdir(exist_ok=True)
                    ip_file = api_dir / f"{test_ip}.json"
                    with open(ip_file, "w", encoding="utf-8") as f:
                        json.dump(r, f, ensure_ascii=False, indent=2)
                
                status_icon = "✓" if r["status"] == "success" else "✗"
                print(f"  {status_icon} [{r['elapsed_ms']:>6.0f}ms] {r['name']:<25} - {r['status']}")
    
    # 保存结果
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    
    # 按状态分组保存
    success_results = [r for r in results if r["status"] == "success"]
    failed_results = [r for r in results if r["status"] != "success"]
    
    # 构建IP索引映射，按TEST_IPS顺序排序
    ip_order = {ip: idx for idx, ip in enumerate(TEST_IPS)}
    
    # 排序：先按API名称，再按IP顺序
    def sort_key(r):
        return (r["name"], ip_order.get(r["test_ip"], 999))
    
    success_results.sort(key=sort_key)
    failed_results.sort(key=sort_key)
    results.sort(key=sort_key)
    
    # 汇总文件
    summary = {
        "total": len(results),
        "success": len(success_results),
        "failed": len(failed_results),
        "concurrency": concurrency,
        "test_ips": TEST_IPS,
        "timestamp": timestamp
    }
    
    with open(output_dir / f"summary_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    # 成功的结果
    with open(output_dir / f"success_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(success_results, f, ensure_ascii=False, indent=2)
    
    # 失败的结果
    with open(output_dir / f"failed_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(failed_results, f, ensure_ascii=False, indent=2)
    
    # 所有结果
    with open(output_dir / f"all_results_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    # 打印汇总
    print("\n" + "=" * 80)
    print(f"测试完成! 成功: {len(success_results)}/{len(results)}")
    print(f"结果已保存到: {output_dir}")
    
    return summary


def main():
    parser = argparse.ArgumentParser(description="IP查询API测试脚本")
    parser.add_argument("-c", "--concurrency", nargs="?", const=-1, type=int, 
                        help="并发数，不传值则自动选择最大并发")
    parser.add_argument("-d", "--deprecated", action="store_true", 
                        help="包含已失效的API")
    parser.add_argument("-v", "--verbose", action="store_true", 
                        help="输出详细JSON文件（每个API单独文件夹）")
    parser.add_argument("--clear", action="store_true", 
                        help="清空旧的JSON文件后再输出")
    
    args = parser.parse_args()
    
    # 确定并发数
    if args.concurrency is None:
        concurrency = 8  # 默认8
    elif args.concurrency == -1:
        import multiprocessing
        concurrency = multiprocessing.cpu_count() * 2  # 自动选择
    else:
        concurrency = args.concurrency
    
    # 运行测试
    asyncio.run(run_tests(concurrency, args.deprecated, args.verbose, args.clear))


if __name__ == "__main__":
    main()
