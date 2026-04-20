#!/usr/bin/env python3
"""更新README中的API状态表格"""

import json
import re
from pathlib import Path

# API配置 (名称, 支持IP查询, 分类, URL模板)
API_CONFIG = {
    "ip-api.com": {"name": "ip-api.com", "supports_ip": True, "category": 1, "url": "http://ip-api.com/json/{ip}?lang=zh-CN"},
    "demo.ip-api.com": {"name": "demo.ip-api.com", "supports_ip": True, "category": 1, "url": "http://demo.ip-api.com/json/{ip}?fields=66842623&lang=zh-CN"},
    "pconline": {"name": "pconline", "supports_ip": True, "category": 1, "url": "https://whois.pconline.com.cn/ipJson.jsp?ip={ip}&json=true"},
    "ip.sb": {"name": "ip.sb", "supports_ip": True, "category": 1, "url": "https://api.ip.sb/geoip/{ip}"},
    "ip2location.io": {"name": "ip2location.io", "supports_ip": True, "category": 1, "url": "https://api.ip2location.io/?ip={ip}"},
    "realip.cc": {"name": "realip.cc", "supports_ip": True, "category": 1, "url": "https://realip.cc/?ip={ip}"},
    "ipapi.co": {"name": "ipapi.co", "supports_ip": True, "category": 1, "url": "https://ipapi.co/json/?ip={ip}"},
    "ipapi.is": {"name": "ipapi.is", "supports_ip": True, "category": 1, "url": "https://ipapi.is/json/{ip}"},
    "db-ip.com": {"name": "db-ip.com", "supports_ip": True, "category": 1, "url": "https://db-ip.com/pd/{ip}"},
    "freeipapi.com": {"name": "freeipapi.com", "supports_ip": True, "category": 1, "url": "https://ipapi.freemie.com/json/{ip}"},
    "ipwhois.app": {"name": "ipwhois.app", "supports_ip": True, "category": 1, "url": "https://ipwhois.app/json/{ip}"},
    "ip.nc.gy": {"name": "ip.nc.gy", "supports_ip": True, "category": 1, "url": "https://ip.nc.gy/{ip}.json"},
    "geojs.io": {"name": "geojs.io", "supports_ip": True, "category": 1, "url": "https://geojs.io/v1/ip/{ip}"},
    "baidu.opendata": {"name": "baidu.opendata", "supports_ip": True, "category": 1, "url": "https://opendata.baidu.com/api.php?resource_id=6006&query={ip}"},
    "httpbin.org": {"name": "httpbin.org", "supports_ip": False, "category": 2, "url": "https://httpbin.org/ip"},
    "cdid.ctrip": {"name": "cdid.ctrip", "supports_ip": False, "category": 2, "url": "https://cdid.ctrip.com/destination/flighthotels/getIP?"},
    "qq.video": {"name": "qq.video", "supports_ip": False, "category": 2, "url": "https://v.qq.com/pub/ip/"},
    "test.ipw.cn": {"name": "test.ipw.cn", "supports_ip": False, "category": 2, "url": "http://test.ipw.cn/"},
    "api.ipify.org": {"name": "api.ipify.org", "supports_ip": False, "category": 2, "url": "https://api.ipify.org/?api=ip"},
    "my.ipinfo.app": {"name": "my.ipinfo.app", "supports_ip": False, "category": 2, "url": "https://my.ipinfo.app/"},
    "g3.letv": {"name": "g3.letv", "supports_ip": False, "category": 2, "url": "https://ip3.le.com/?"},
    "qq.inews": {"name": "qq.inews", "supports_ip": False, "category": 2, "url": "https://r.inews.qq.com/api/ip2city"},
    "myip.ipip.net": {"name": "myip.ipip.net", "supports_ip": False, "category": 2, "url": "https://myip.ipip.net/"},
    "ifconfig.me": {"name": "ifconfig.me", "supports_ip": False, "category": 2, "url": "https://ifconfig.me/json"},
    "geolocation-db.com": {"name": "geolocation-db.com", "supports_ip": False, "category": 2, "url": "https://geolocation-db.com/json/"},
    "api.myip.com": {"name": "api.myip.com", "supports_ip": False, "category": 2, "url": "https://api.myip.com/v2/"},
    "wtfismyip.com": {"name": "wtfismyip.com", "supports_ip": False, "category": 2, "url": "https://wtfismyip.com/json"},
    "ipbase.com": {"name": "ipbase.com", "supports_ip": False, "category": 2, "url": "https://ipbase.com/"},
    "ipquery.io": {"name": "ipquery.io", "supports_ip": False, "category": 2, "url": "https://api.ipquery.io/"},
    "cloudflare.trace": {"name": "cloudflare.trace", "supports_ip": False, "category": 2, "url": "https://www.cloudflare.com/cdn-cgi/trace"},
    "torproject": {"name": "torproject", "supports_ip": False, "category": 2, "url": "https://check.torproject.org/"},
    "bilibili": {"name": "bilibili", "supports_ip": False, "category": 2, "url": "https://api.bilibili.com/x/user/web/live_ip"},
    "news.qq": {"name": "news.qq", "supports_ip": False, "category": 2, "url": "https://r.inews.qq.com/api/ip2city"},
    "gdt.qq": {"name": "gdt.qq", "supports_ip": False, "category": 2, "url": "https://r.inews.qq.com/api/ip2city"},
    "cip.cc": {"name": "cip.cc", "supports_ip": True, "category": 2, "url": "http://www.cip.cc/{ip}"},
    "ipinfo.io": {"name": "ipinfo.io", "supports_ip": True, "category": 3, "url": "https://ipinfo.io/{ip}/json"},
    "db-ip.demo": {"name": "db-ip.demo", "supports_ip": True, "category": 3, "url": "https://db-ip.com/pd/{ip}"},
    "iqiyi.mesh": {"name": "iqiyi.mesh", "supports_ip": True, "category": 3, "url": "https://pc-bridge.iqiyi.com/ips"},
}


def get_api_status(api_name: str) -> dict:
    """获取API状态"""
    api_dir = Path(__file__).parent.parent / "output" / "by_api" / api_name
    if not api_dir.exists():
        return {"status": "unknown", "elapsed_ms": None, "count": 0, "success": 0, "failed": 0}
    
    results = list(api_dir.glob("*.json"))
    if not results:
        return {"status": "unknown", "elapsed_ms": None, "count": 0, "success": 0, "failed": 0}
    
    success_count = 0
    failed_count = 0
    total_elapsed = 0
    
    for result_file in results:
        try:
            with open(result_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data.get("status") == "success":
                    success_count += 1
                    total_elapsed += data.get("elapsed_ms", 0)
                else:
                    failed_count += 1
        except Exception:
            failed_count += 1
    
    avg_elapsed = round(total_elapsed / success_count, 2) if success_count > 0 else None
    
    if failed_count == 0 and success_count > 0:
        status = "success"
    elif success_count == 0:
        status = "failed"
    else:
        status = "partial"
    
    return {
        "status": status,
        "elapsed_ms": avg_elapsed,
        "count": len(results),
        "success": success_count,
        "failed": failed_count
    }


def get_status_icon(status: str) -> str:
    """获取状态图标"""
    icons = {
        "success": "✅",
        "failed": "❌",
        "partial": "⚠️",
        "unknown": "❓"
    }
    return icons.get(status, "❓")


def generate_readme_table() -> str:
    """生成README中的API状态表格"""
    from datetime import datetime
    from urllib.parse import quote
    update_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    test_ips = ["117.30.120.138", "1.1.1.1", "8.8.8.8"]
    test_ip = test_ips[0]
    test_ips_str = ", ".join(test_ips)
    
    output_lines = []
    output_lines.append("## 📊 API状态监控\n")
    output_lines.append(f"> Updated at UTC+0: {update_time}\n")
    output_lines.append(f"> 由 GitHub Actions 自动更新于 (UTC+8): {update_time}\n")
    output_lines.append(f"> 测试IP: {test_ips_str}\n")
    output_lines.append("### 支持查询指定IP的API\n")
    output_lines.append("| 测试 | API | 状态 | 平均响应 | 成功率 | 详情 |")
    output_lines.append("|------|-----|------|---------|--------|------|")
    
    for api_name, config in sorted(API_CONFIG.items()):
        if config["category"] != 1:
            continue
        stat = get_api_status(api_name)
        icon = get_status_icon(stat["status"])
        elapsed = f"{stat['elapsed_ms']}ms" if stat["elapsed_ms"] else "-"
        success_rate = f"{stat['success']}/{stat['count']}" if stat["count"] > 0 else "-"
        url = config.get("url", "").replace("{ip}", test_ip)
        badge_url = f"https://img.shields.io/website?url={quote(url, safe='')}&label={api_name}"
        shield_link = f"[![{api_name}]({badge_url})]({url})"
        detail_link = f"[📁 查看](output/by_api/{api_name}/)"
        output_lines.append(f"| {shield_link} | {api_name} | {icon} | {elapsed} | {success_rate} | {detail_link} |")
    
    output_lines.append("\n### 仅查询本机IP的API\n")
    output_lines.append("| 测试 | API | 状态 | 平均响应 | 成功率 | 详情 |")
    output_lines.append("|------|-----|------|---------|--------|------|")
    
    for api_name, config in sorted(API_CONFIG.items()):
        if config["category"] != 2:
            continue
        stat = get_api_status(api_name)
        icon = get_status_icon(stat["status"])
        elapsed = f"{stat['elapsed_ms']}ms" if stat["elapsed_ms"] else "-"
        success_rate = f"{stat['success']}/{stat['count']}" if stat["count"] > 0 else "-"
        url = config.get("url", "")
        badge_url = f"https://img.shields.io/website?url={quote(url, safe='')}&label={api_name}"
        shield_link = f"[![{api_name}]({badge_url})]({url})"
        detail_link = f"[📁 查看](output/by_api/{api_name}/)"
        output_lines.append(f"| {shield_link} | {api_name} | {icon} | {elapsed} | {success_rate} | {detail_link} |")
    
    output_lines.append("\n### 仅支持查询指定IP的API\n")
    output_lines.append("| 测试 | API | 状态 | 平均响应 | 成功率 | 详情 |")
    output_lines.append("|------|-----|------|---------|--------|------|")
    
    for api_name, config in sorted(API_CONFIG.items()):
        if config["category"] != 3:
            continue
        stat = get_api_status(api_name)
        icon = get_status_icon(stat["status"])
        elapsed = f"{stat['elapsed_ms']}ms" if stat["elapsed_ms"] else "-"
        success_rate = f"{stat['success']}/{stat['count']}" if stat["count"] > 0 else "-"
        url = config.get("url", "").replace("{ip}", test_ip)
        badge_url = f"https://img.shields.io/website?url={quote(url, safe='')}&label={api_name}"
        shield_link = f"[![{api_name}]({badge_url})]({url})"
        detail_link = f"[📁 查看](output/by_api/{api_name}/)"
        output_lines.append(f"| {shield_link} | {api_name} | {icon} | {elapsed} | {success_rate} | {detail_link} |")
    
    return "\n".join(output_lines)


def update_readme():
    """更新README文件"""
    readme_path = Path(__file__).parent.parent / "README.md"
    
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 查找 <!-- API_STATUS_START --> 和 <!-- API_STATUS_END --> 之间的内容
    pattern = r"<!-- API_STATUS_START -->.*?<!-- API_STATUS_END -->"
    new_table = generate_readme_table()
    placeholder = f"<!-- API_STATUS_START -->\n{new_table}\n<!-- API_STATUS_END -->"
    
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, placeholder, content, flags=re.DOTALL)
    else:
        # 如果没有占位符，添加到文件末尾
        content += "\n\n" + placeholder
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("README.md updated successfully!")


if __name__ == "__main__":
    update_readme()
