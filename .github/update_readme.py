#!/usr/bin/env python3
"""更新README中的API状态表格"""

import json
import re
from pathlib import Path

# API配置 (名称, 支持IP查询, 分类)
API_CONFIG = {
    "ip-api.com": {"name": "ip-api.com", "supports_ip": True, "category": 1},
    "demo.ip-api.com": {"name": "demo.ip-api.com", "supports_ip": True, "category": 1},
    "pconline": {"name": "pconline", "supports_ip": True, "category": 1},
    "ip.sb": {"name": "ip.sb", "supports_ip": True, "category": 1},
    "ip2location.io": {"name": "ip2location.io", "supports_ip": True, "category": 1},
    "realip.cc": {"name": "realip.cc", "supports_ip": True, "category": 1},
    "ipapi.co": {"name": "ipapi.co", "supports_ip": True, "category": 1},
    "ipapi.is": {"name": "ipapi.is", "supports_ip": True, "category": 1},
    "db-ip.com": {"name": "db-ip.com", "supports_ip": True, "category": 1},
    "freeipapi.com": {"name": "freeipapi.com", "supports_ip": True, "category": 1},
    "ipwhois.app": {"name": "ipwhois.app", "supports_ip": True, "category": 1},
    "ip.nc.gy": {"name": "ip.nc.gy", "supports_ip": True, "category": 1},
    "geojs.io": {"name": "geojs.io", "supports_ip": True, "category": 1},
    "baidu.opendata": {"name": "baidu.opendata", "supports_ip": True, "category": 1},
    "httpbin.org": {"name": "httpbin.org", "supports_ip": False, "category": 2},
    "cdid.ctrip": {"name": "cdid.ctrip", "supports_ip": False, "category": 2},
    "qq.video": {"name": "qq.video", "supports_ip": False, "category": 2},
    "test.ipw.cn": {"name": "test.ipw.cn", "supports_ip": False, "category": 2},
    "api.ipify.org": {"name": "api.ipify.org", "supports_ip": False, "category": 2},
    "my.ipinfo.app": {"name": "my.ipinfo.app", "supports_ip": False, "category": 2},
    "g3.letv": {"name": "g3.letv", "supports_ip": False, "category": 2},
    "qq.inews": {"name": "qq.inews", "supports_ip": False, "category": 2},
    "myip.ipip.net": {"name": "myip.ipip.net", "supports_ip": False, "category": 2},
    "ifconfig.me": {"name": "ifconfig.me", "supports_ip": False, "category": 2},
    "geolocation-db.com": {"name": "geolocation-db.com", "supports_ip": False, "category": 2},
    "api.myip.com": {"name": "api.myip.com", "supports_ip": False, "category": 2},
    "wtfismyip.com": {"name": "wtfismyip.com", "supports_ip": False, "category": 2},
    "ipbase.com": {"name": "ipbase.com", "supports_ip": False, "category": 2},
    "ipquery.io": {"name": "ipquery.io", "supports_ip": False, "category": 2},
    "cloudflare.trace": {"name": "cloudflare.trace", "supports_ip": False, "category": 2},
    "torproject": {"name": "torproject", "supports_ip": False, "category": 2},
    "bilibili": {"name": "bilibili", "supports_ip": False, "category": 2},
    "news.qq": {"name": "news.qq", "supports_ip": False, "category": 2},
    "gdt.qq": {"name": "gdt.qq", "supports_ip": False, "category": 2},
    "cip.cc": {"name": "cip.cc", "supports_ip": True, "category": 2},
    "ipinfo.io": {"name": "ipinfo.io", "supports_ip": True, "category": 3},
    "db-ip.demo": {"name": "db-ip.demo", "supports_ip": True, "category": 3},
    "iqiyi.mesh": {"name": "iqiyi.mesh", "supports_ip": True, "category": 3},
}


def get_api_status(api_name: str) -> dict:
    """获取API状态"""
    api_dir = Path(__file__).parent.parent / "test" / "output" / "by_api" / api_name
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
    output_lines = []
    output_lines.append("## 📊 API状态监控\n")
    output_lines.append(f"> 自动更新于: test/output\n")
    output_lines.append("### 支持查询指定IP的API\n")
    output_lines.append("| API | 状态 | 平均响应 | 成功率 | 详情 |")
    output_lines.append("|-----|------|---------|--------|------|")
    
    for api_name, config in sorted(API_CONFIG.items()):
        if config["category"] != 1:
            continue
        stat = get_api_status(api_name)
        icon = get_status_icon(stat["status"])
        elapsed = f"{stat['elapsed_ms']}ms" if stat["elapsed_ms"] else "-"
        success_rate = f"{stat['success']}/{stat['count']}" if stat["count"] > 0 else "-"
        detail_link = f"[📁 查看](test/output/by_api/{api_name}/)"
        output_lines.append(f"| {api_name} | {icon} | {elapsed} | {success_rate} | {detail_link} |")
    
    output_lines.append("\n### 仅查询本机IP的API\n")
    output_lines.append("| API | 状态 | 平均响应 | 成功率 | 详情 |")
    output_lines.append("|-----|------|---------|--------|------|")
    
    for api_name, config in sorted(API_CONFIG.items()):
        if config["category"] != 2:
            continue
        stat = get_api_status(api_name)
        icon = get_status_icon(stat["status"])
        elapsed = f"{stat['elapsed_ms']}ms" if stat["elapsed_ms"] else "-"
        success_rate = f"{stat['success']}/{stat['count']}" if stat["count"] > 0 else "-"
        detail_link = f"[📁 查看](test/output/by_api/{api_name}/)"
        output_lines.append(f"| {api_name} | {icon} | {elapsed} | {success_rate} | {detail_link} |")
    
    output_lines.append("\n### 仅支持查询指定IP的API\n")
    output_lines.append("| API | 状态 | 平均响应 | 成功率 | 详情 |")
    output_lines.append("|-----|------|---------|--------|------|")
    
    for api_name, config in sorted(API_CONFIG.items()):
        if config["category"] != 3:
            continue
        stat = get_api_status(api_name)
        icon = get_status_icon(stat["status"])
        elapsed = f"{stat['elapsed_ms']}ms" if stat["elapsed_ms"] else "-"
        success_rate = f"{stat['success']}/{stat['count']}" if stat["count"] > 0 else "-"
        detail_link = f"[📁 查看](test/output/by_api/{api_name}/)"
        output_lines.append(f"| {api_name} | {icon} | {elapsed} | {success_rate} | {detail_link} |")
    
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
