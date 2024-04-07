# 说明

该存储库收集了各种免费的IP查询API，无需配置任何key直接可访问，使大家能够快速访问IP信息，如地理位置、ISP详细信息和网络类型。请根据自己的需求选择合适的API，持续更新中，欢迎star

&emsp;

### API列表

1.可查询本机IP和通过IP查询信息

[https://webapi-pc.meitu.com/common/ip_location](#address-1.1) 

[https://www.ip.cn/api/index?ip=&type=0](#address-1.2) 

[https://whois.pconline.com.cn/ipJson.jsp?ip=&json=true](#address-1.3) 

[https://api.vore.top/api/IPdata?ip=](#address-1.4) 

[https://api.ip.sb/geoip/](#address-1.5) 

[https://api.ip2location.io/](#address-1.6) 

[https://realip.cc/](#address-1.7)

[http://demo.ip-api.com/json/?lang=zh-CN](#address-1.8)

[https://ip-api.io/json](#address-1.9)

[https://ipapi.co/json/](#address-1.10)

[https://api.ipapi.is](#address-1.11)

[https://api.ip.sb/geoip](#address-1.12)

[https://api.qjqq.cn/api/Local](#address-1.13)

2.只可查询本机(访客)IP信息

[https://ip.useragentinfo.com/json](#address-2.1) 

[http://httpbin.org/ip](#address-2.2) 

[https://cdid.c-ctrip.com/model-poc2/h](#address-2.3) 

[https://vv.video.qq.com/checktime?otype=ojson](#address-2.4) 

[https://api.uomg.com/api/visitor.info?skey=1](#address-2.5) 

[https://test.ipw.cn/api/ip/myip?json](#address-2.6) 

[https://api.ipify.org](#address-2.7) 

[https://ipv4.my.ipinfo.app/api/ipDetails.php](#address-2.8) 

3.只可通过IP查询信息

[http://opendata.baidu.com/api.php?co=&resource_id=6006&oe=utf8&query=](#address-3.1) 

[https://get.geojs.io/v1/ip/geo/121.8.215.106.json](#address-3.2) 

[https://ipinfo.io/widget/demo/121.8.215.106](#address-3.3) 

[https://ipapi.com/ip_api.php?ip=121.8.215.106](#address-3.4) 

[https://db-ip.com/demo/home.php?s=121.8.215.106](#address-3.5) 

4.[只需要获取IP](#address-4.1) 

&emsp;
<a name="address-1.1"></a>

### 1.可查询本机IP和通过IP查询 


**地址①**：https://webapi-pc.meitu.com/common/ip_location?ip=

请求类型：GET

请求参数：ip(可选)

请求示例：

```
# 查询本机ip
https://webapi-pc.meitu.com/common/ip_location

# 通过ip查询信息
https://webapi-pc.meitu.com/common/ip_location?ip=121.8.215.106
```

示例结果：

```
{
  "reqid": "40b7cf49-ad3f-4184-acd3-9f5a574dc7c4",
  "code": 0,
  "data": {
    "121.8.215.106": {
      "area_code": "86",
      "city": "广州市",
      "city_id": 160063402,
      "continent": "亚洲",
      "continent_code": "AP",
      "country_id": 100000,
      "isp": "电信",
      "latitude": 23.3283,
      "longitude": 113.75837,
      "nation": "中国",
      "nation_code": "CN",
      "province": "广东",
      "province_id": 440000,
      "subdivision_1_iso_code": "*",
      "subdivision_1_name": "广东",
      "subdivision_2_iso_code": "*",
      "subdivision_2_name": "广州市",
      "time_zone": "UTC+8"
    }
  }
}
```

&emsp;

**地址②**：https://www.ip.cn/api/index?ip=&type=0 <a name="address-1.2"></a>

请求类型：GET

请求参数：ip(可选)、type

请求示例：

```
# 查询本机ip(type=0)
https://www.ip.cn/api/index?ip=&type=0

# 通过ip查询信息(type=1)
https://www.ip.cn/api/index?ip=121.8.215.106&type=1
```

> 对于国外ip的位置信息不太准确

示例结果：

```
{
  "rs": 1,
  "code": 0,
  "address": "中国  广东省 广州市 电信",
  "ip": "121.8.215.106",
  "isDomain": 0
}
```

&emsp;

**地址③**：https://whois.pconline.com.cn/ipJson.jsp?ip=&json=true <a name="address-1.3"></a>

请求类型：GET

请求参数(可选)：ip、json

请求示例：

```
# 查询本机ip
https://whois.pconline.com.cn/ipJson.jsp?ip=&json=true

# 通过ip查询信息
https://whois.pconline.com.cn/ipJson.jsp?ip=121.8.215.106&json=true
```

> 对于国外ip的位置信息不太准确

示例结果：

```
{
  "ip": "121.8.215.106",
  "pro": "广东省",
  "proCode": "440000",
  "city": "广州市",
  "cityCode": "440100",
  "region": "",
  "regionCode": "0",
  "addr": "广东省广州市 电信",
  "regionNames": "",
  "err": ""
}
```

&emsp;

**地址④**：https://api.vore.top/api/IPdata?ip= <a name="address-1.4"></a>

请求类型：GET

请求参数(可选)：ip

请求示例：

```
# 查询本机ip
https://api.vore.top/api/IPdata?ip=

# 通过ip查询信息
https://api.vore.top/api/IPdata?ip=121.8.215.106
```

示例结果：

```
{
    "code": 200,
    "msg": "SUCCESS",
    "ipinfo": {
        "type": "ipv4",
        "text": "121.8.215.106",
        "cnip": true
    },
    "ipdata": {
        "info1": "广东省",
        "info2": "广州市",
        "info3": "增城",
        "isp": "电信"
    },
    "adcode": {
        "o": "广东省广州市增城 - 电信",
        "p": "广东",
        "c": "广州",
        "n": "广东-广州",
        "r": "广东-广州",
        "a": "440100",
        "i": true
    },
    "tips": "接口由VORE-API(https:\/\/api.vore.top\/)免费提供",
    "time": 1708576755
}
```

&emsp;

**地址⑤**：https://api.ip.sb/geoip/ <a name="address-1.5"></a>

请求类型：GET

请求参数(可选)：你的ip

请求示例：

```
# 查询本机ip
https://api.ip.sb/geoip/

# 通过ip查询信息
https://api.ip.sb/geoip/121.8.215.106
```

示例结果：

```
{
    "organization": "China Telecom",
    "longitude": 113.2539,
    "city": "Guangzhou",
    "timezone": "Asia/Shanghai",
    "isp": "China Telecom",
    "offset": 28800,
    "region": "Guangdong",
    "asn": 4134,
    "asn_organization": "Chinanet",
    "country": "China",
    "ip": "121.8.215.106",
    "latitude": 23.1181,
    "continent_code": "AS",
    "country_code": "CN",
    "region_code": "GD"
}
```

&emsp;

**地址⑥**：https://api.ip2location.io/ <a name="address-1.6"></a>

请求类型：GET

请求参数(可选)：ip

请求示例：

```
# 查询本机ip
https://api.ip2location.io/

# 通过ip查询信息
https://api.ip2location.io/?ip=121.8.215.106
```

示例结果：

```
{
  "ip": "121.8.215.106",
  "country_code": "CN",
  "country_name": "China",
  "region_name": "Guangdong",
  "city_name": "Guangzhou",
  "latitude": 23.127361,
  "longitude": 113.26457,
  "zip_code": "510140",
  "time_zone": "+08:00",
  "asn": "4134",
  "as": "Asia Pacific Network Information Centre",
  "is_proxy": true,
  "message": "Limit to 500 queries per day. Sign up for a Free plan at https://www.ip2location.io to get 30K queries per month."
}
```

&emsp;

**地址⑦**：https://realip.cc/ <a name="address-1.7"></a>

请求类型：GET

请求参数(可选)：ip

请求示例：

```
# 查询本机ip

curl realip.cc

https://realip.cc/

https://realip.cc/simple # 只返回ip

# 通过ip查询信息
https://realip.cc/?ip=121.8.215.106

```

示例结果：

```
{
    "ip": "103.143.161.60",
    "city": "Hong Kong",
    "province": null,
    "country": "Hong Kong",
    "continent": "Asia",
    "isp": "TWOWIN CO., LIMITED",
    "time_zone": "Asia/Hong_Kong",
    "latitude": 22.2842,
    "longitude": 114.1759,
    "postal_code": null,
    "iso_code": "HK",
    "network": "103.143.160.0/23",
    "notice": "api文档在/docs路径下，调用并发数是有限制的 ©2021-09-27->now",
    "provider": "Powered by Bboysoul",
    "blog": "https://www.bboy.app",
    "tg_group": "https://t.me/bboyapp",
    "data_updatetime": 202403010,
    "count": 10345364
}
```

&emsp;

**地址⑧**：http://demo.ip-api.com/json/?fields=66842623&lang=zh-CN <a name="address-1.8"></a>

请求类型：GET

请求参数(可选)：ip、lang ...

请求示例：

```
# lang optional value
en：English (default) 英语（默认）
zh-CN：中国 (Chinese)
de：Deutsch (German) Deutsch （德语）
es：Español (Spanish) Español （西班牙语）
fr：Français (French) Français （法语）
ja：日本語 (Japanese) 日本语（ Japanese）
ru：Русский (Russian) Русский （俄语）

# 注意是http ！！！

# 查询本机ip
http://demo.ip-api.com/json/?fields=66842623&lang=zh-CN

# 通过ip查询信息
http://demo.ip-api.com/json/121.8.215.106?fields=66842623&lang=zh-CN

API docs：
https://ip-api.com/docs/api:json
```

示例结果：

```
{
    "status": "success",
    "continent": "亚洲",
    "continentCode": "AS",
    "country": "中国",
    "countryCode": "CN",
    "region": "GD",
    "regionName": "广东",
    "city": "广州市",
    "district": "",
    "zip": "",
    "lat": 23.1181,
    "lon": 113.2539,
    "timezone": "Asia/Shanghai",
    "offset": 28800,
    "currency": "CNY",
    "isp": "Chinanet",
    "org": "Chinanet GD",
    "as": "AS4134 CHINANET-BACKBONE",
    "asname": "CHINANET-BACKBONE",
    "mobile": false,
    "proxy": true,
    "hosting": false,
    "query": "121.8.215.106"
}
```

&emsp;

**地址⑨**：https://ip-api.io/json <a name="address-1.9"></a>

请求类型：GET

请求参数(可选)：ip

请求示例：

```
# 查询本机ip
https://ip-api.io/json

# 通过ip查询信息
https://ip-api.io/json?ip=121.8.215.106
```

示例结果：

```
{
    "callingCode": "86",
    "city": "Guangzhou",
    "countryCapital": "Beijing",
    "country_code": "CN",
    "country_name": "China",
    "currency": "CNY",
    "currencySymbol": "¥",
    "emojiFlag": "🇨🇳",
    "flagUrl": "https://ip-api.io/images/flags/cn.svg",
    "ip": "121.8.215.106",
    "is_in_european_union": false,
    "latitude": 23.1181,
    "longitude": 113.2539,
    "metro_code": 0,
    "organisation": "Chinanet",
    "region_code": "GD",
    "region_name": "Guangdong",
    "suspiciousFactors": {
        "isProxy": false,
        "isSpam": false,
        "isSuspicious": false,
        "isTorNode": false
    },
    "time_zone": "Asia/Shanghai",
    "zip_code": ""
}
```

&emsp;

**地址⑩**：https://ipapi.co/json <a name="address-1.10"></a>

请求类型：GET

请求参数(可选)：ip

请求示例：

```
# 查询本机ip
https://ipapi.co/json/

# 通过ip查询信息
https://ipapi.co/121.8.215.106/json/
```

示例结果：

```
{
    "ip": "121.8.215.106",
    "network": "121.8.128.0/17",
    "version": "IPv4",
    "city": "Guangzhou",
    "region": "Guangdong",
    "region_code": "GD",
    "country": "CN",
    "country_name": "China",
    "country_code": "CN",
    "country_code_iso3": "CHN",
    "country_capital": "Beijing",
    "country_tld": ".cn",
    "continent_code": "AS",
    "in_eu": false,
    "postal": null,
    "latitude": 23.1181,
    "longitude": 113.2539,
    "timezone": "Asia/Shanghai",
    "utc_offset": "+0800",
    "country_calling_code": "+86",
    "currency": "CNY",
    "currency_name": "Yuan Renminbi",
    "languages": "zh-CN,yue,wuu,dta,ug,za",
    "country_area": 9596960,
    "country_population": 1411778724,
    "asn": "AS4134",
    "org": "Chinanet"
}
```

&emsp;

**地址11**：https://ipapi.co/json <a name="address-1.11"></a>

请求类型：GET

请求参数(可选)：ip

请求示例：

```
# 查询本机ip
https://api.ipapi.is

# 通过ip查询信息
https://api.ipapi.is/?ip=121.8.215.106
```

示例结果：

```
{
    "ip": "121.8.215.106",
    "rir": "APNIC",
    "is_bogon": false,
    "is_mobile": false,
    "is_crawler": false,
    "is_datacenter": false,
    "is_tor": false,
    "is_proxy": true,
    "is_vpn": false,
    "is_abuser": true,
    "company": {
        "name": "CHINANET Guangdong province network",
        "abuser_score": "0.0003 (Very Low)",
        "domain": "chinatelecom.cn",
        "type": "isp",
        "network": "121.8.0.0 - 121.15.255.255",
        "whois": "https://api.ipapi.is/?whois=121.8.0.0"
    },
    "asn": {
        "asn": 4134,
        "abuser_score": "0.0013 (Low)",
        "route": "121.8.0.0/13",
        "descr": "CHINANET-BACKBONE No.31,Jin-rong Street, CN",
        "country": "cn",
        "active": true,
        "org": "No.31,Jin-rong Street",
        "domain": "chinatelecom.cn",
        "abuse": "anti-spam@chinatelecom.cn",
        "type": "business",
        "updated": "2021-06-15",
        "rir": "APNIC",
        "whois": "https://api.ipapi.is/?whois=AS4134"
    },
    "location": {
        "continent": "AS",
        "country": "China",
        "country_code": "CN",
        "state": "Guangdong",
        "city": "Guangzhou",
        "latitude": 23.117,
        "longitude": 113.25,
        "zip": "510800",
        "timezone": "Asia/Shanghai",
        "local_time": "2024-03-16T13:50:41+08:00",
        "local_time_unix": 1710568241,
        "is_dst": false
    },
    "elapsed_ms": 0.81
}
```

&emsp;

**地址12**：https://api.ip.sb/geoip <a name="address-1.12"></a>

请求类型：GET

请求参数(可选)：ip

请求示例：

```
# 查询本机ip
https://api.ip.sb/geoip

# 通过ip查询信息
https://api.ip.sb/geoip/121.8.215.106
```

示例结果：

```
{
    "organization": "China Telecom",
    "longitude": 113.2539,
    "city": "Guangzhou",
    "timezone": "Asia/Shanghai",
    "isp": "China Telecom",
    "offset": 28800,
    "region": "Guangdong",
    "asn": 4134,
    "asn_organization": "Chinanet",
    "country": "China",
    "ip": "121.8.215.106",
    "latitude": 23.1181,
    "continent_code": "AS",
    "country_code": "CN",
    "region_code": "GD"
}
```

&emsp;

**地址13**：https://api.qjqq.cn/api/Local <a name="address-1.13"></a>

请求类型：GET

请求参数(可选)：ip

请求示例：

```
# 查询本机ip
https://api.qjqq.cn/api/Local

# 通过ip查询信息
https://api.qjqq.cn/api/district?ip=121.8.215.106
```

示例结果：

```
{
  "code": 200,
  "data": {
    "ip": "222.79.44.74",
    "continent": "亚洲",
    "country_english": "",
    "country": "中国",
    "prov": "福建",
    "city": "福州",
    "district": "",
    "isp": "电信",
    "lat": "26.075302",
    "lng": "119.306239",
    "area_code": "350100",
    "city_code": "0591",
    "elevation": "29",
    "time_zone": "Asia/Shanghai",
    "weather_station": "CHXX0031",
    "zip_code": "350000"
  },
  "msg": "success",
  "ip": "222.79.44.74",
  "time": "2024-04-07 18:38:08",
  "source": "青桔API：api.qjqq.cn"
}
```

&emsp;

<a name="address-2.1"></a>

### 2.只可查询本机IP 

**地址①**：https://ip.useragentinfo.com/json

请求类型：GET

请求参数：无

请求示例：

```
https://ip.useragentinfo.com/json
```

示例结果：

```
{
  "country": "韩国",
  "short_name": "KR",
  "province": "首尔",
  "city": "",
  "area": "",
  "isp": "微软云",
  "net": "数据中心",
  "ip": "20.249.16.173",
  "code": 200,
  "desc": "success"
}
```

&emsp;

**地址②**：http://httpbin.org/ip <a name="address-2.2"></a>

请求类型：GET

请求参数：无

请求示例：

```
http://httpbin.org/ip
```

示例结果：

```
{
  "origin": "20.249.16.173"
}
```

&emsp;

**地址③**：https://cdid.c-ctrip.com/model-poc2/h <a name="address-2.3"></a>

请求类型：GET

请求参数：无

请求示例：

```
https://cdid.c-ctrip.com/model-poc2/h
```

示例结果：

```
20.249.16.173
```

&emsp;

**地址④**：https://vv.video.qq.com/checktime?otype=ojson <a name="address-2.4"></a>

请求类型：GET

请求参数：otype

请求示例：

```
https://vv.video.qq.com/checktime?otype=ojson
```

> otype=json时返回类型为jsonp

示例结果：

```
{
  "s": "o",
  "t": 1708586979,
  "ip": "222.79.47.146",
  "pos": "---",
  "rand": "FRM_cmo206yshBHl5h4_9A=="
}
```

&emsp;

**地址⑤**：https://api.uomg.com/api/visitor.info?skey=1 <a name="address-2.5"></a>

请求类型：GET

请求参数：无

请求示例：

```
https://api.uomg.com/api/visitor.info?skey=1
```

示例结果：

```
{
  "code": 1,
  "ip": "20.249.16.173",
  "system": "Windows 10 x64 Edition",
  "browser": "Chrome 114.0.0.0",
  "time": "2024-02-22 15:37:33"
}
```

&emsp;

**地址⑥**：https://test.ipw.cn/api/ip/myip?json <a name="address-2.6"></a>

请求类型：GET

请求参数：无

请求示例：

```
https://test.ipw.cn/api/ip/myip?json
```

示例结果：

```
{
  "code": 1,
  "ip": "20.249.16.173",
  "system": "Windows 10 x64 Edition",
  "browser": "Chrome 114.0.0.0",
  "time": "2024-02-22 15:37:33"
}
```

&emsp;

**地址⑦**：https://api.ipify.org <a name="address-2.7"></a>

请求类型：GET

请求参数（可选）：format

请求示例：

```
format：text, json, jsonp

# IPv4
https://api.ipify.org?format=json

# IPv6
https://api64.ipify.org/?format=json
```

示例结果：

```
{
    "ip": "185.151.146.112"
}
```

&emsp;

**地址⑧**：https://ipv4.my.ipinfo.app/api/ipDetails.php <a name="address-2.8"></a>

请求类型：GET

请求参数：无

请求示例：

```
https://ipv4.my.ipinfo.app/api/ipDetails.php
```

示例结果：

```
{
    "ip": "8.210.218.24",
    "asn": "AS45102 ALIBABA-CN-NET Alibaba US Technology Co., Ltd., CN",
    "continent": "AS",
    "continentLong": "Asia",
    "flag": "https://my.ipinfo.app/imgs/flags/4x3/sg.svg",
    "country": "Singapore"
}
```

&emsp;

<a name="address-3.1"></a>

### 3.只可通过IP查询 

**地址①**：http://opendata.baidu.com/api.php?co=&resource_id=6006&oe=utf8&query=

请求类型：GET

请求参数：query

请求示例：

```
https://opendata.baidu.com/api.php?co=&resource_id=6006&oe=utf8&query=121.8.215.106
```

示例结果：

```
{
  "status": "0",
  "t": "",
  "set_cache_time": "",
  "data": [
    {
      "ExtendedLocation": "",
      "OriginQuery": "121.8.215.106",
      "appinfo": "",
      "disp_type": 0,
      "fetchkey": "121.8.215.106",
      "location": "广东省广州市 电信",
      "origip": "121.8.215.106",
      "origipquery": "121.8.215.106",
      "resourceid": "6006",
      "role_id": 0,
      "shareImage": 1,
      "showLikeShare": 1,
      "showlamp": "1",
      "titlecont": "IP地址查询",
      "tplt": "ip"
    }
  ]
}
```

&emsp;

**地址②**：https://get.geojs.io/v1/ip/geo/121.8.215.106.json <a name="address-3.2"></a>

请求类型：GET

请求参数：你的ip

请求示例：

```
https://get.geojs.io/v1/ip/geo/121.8.215.106.json
```

示例结果：

```
{
    "country": "China",
    "timezone": "Asia/Shanghai",
    "ip": "121.8.215.106",
    "organization": "AS4134 Chinanet",
    "asn": 4134,
    "area_code": "0",
    "organization_name": "Chinanet",
    "country_code": "CN",
    "country_code3": "CHN",
    "continent_code": "AS",
    "latitude": "23.1181",
    "region": "Guangdong",
    "city": "Guangzhou",
    "longitude": "113.2539",
    "accuracy": 1000
}
```

&emsp;

**地址③**：https://ipinfo.io/widget/demo/121.8.215.106 <a name="address-3.3"></a>

请求类型：GET

请求参数：你的ip

请求示例：

```
https://ipinfo.io/widget/demo/121.8.215.106
```

示例结果：

```
{
    "input": "121.8.215.106",
    "data": {
        "ip": "121.8.215.106",
        "city": "Shenzhen",
        "region": "Guangdong",
        "country": "CN",
        "loc": "22.5455,114.0683",
        "org": "AS4134 CHINANET-BACKBONE",
        "timezone": "Asia/Shanghai",
        "asn": {
            "asn": "AS4134",
            "name": "CHINANET-BACKBONE",
            "domain": "chinatelecom.com.cn",
            "route": "121.8.0.0/13",
            "type": "isp"
        },
        "company": {
            "name": "CHINANET Guangdong province network",
            "domain": "chinatelecom.cn",
            "type": "isp"
        },
        "privacy": {
            "vpn": false,
            "proxy": false,
            "tor": false,
            "relay": false,
            "hosting": false,
            "service": ""
        },
        "abuse": {
            "address": "No.31 ,jingrong street,beijing, 100032",
            "country": "CN",
            "email": "anti-spam@chinatelecom.cn",
            "name": "ABUSE CHINANETCN",
            "network": "121.8.0.0/13",
            "phone": "+000000000"
        }
    }
}
```

&emsp;

**地址④**：https://ipapi.com/ip_api.php?ip=121.8.215.106 <a name="address-3.4"></a>

请求类型：GET

请求参数：ip

请求示例：

```
https://ipapi.com/ip_api.php?ip=121.8.215.106
```

示例结果：

```
{
    "ip": "121.8.215.106",
    "hostname": "121.8.215.106",
    "type": "ipv4",
    "continent_code": "AS",
    "continent_name": "Asia",
    "country_code": "CN",
    "country_name": "China",
    "region_code": "GD",
    "region_name": "Guangdong",
    "city": "Guangzhou",
    "zip": "510000",
    "latitude": 23.124719619750977,
    "longitude": 113.23860931396484,
    "location": {
        "geoname_id": 1809858,
        "capital": "Beijing",
        "languages": [
            {
                "code": "zh",
                "name": "Chinese",
                "native": "中文"
            }
        ],
        "country_flag": "https://assets.ipstack.com/flags/cn.svg",
        "country_flag_emoji": "🇨🇳",
        "country_flag_emoji_unicode": "U+1F1E8 U+1F1F3",
        "calling_code": "86",
        "is_eu": false
    },
    "time_zone": {
        "id": "Asia/Shanghai",
        "current_time": "2024-03-15T15:14:15+08:00",
        "gmt_offset": 28800,
        "code": "CST",
        "is_daylight_saving": false
    },
    "currency": {
        "code": "CNY",
        "name": "Chinese Yuan",
        "plural": "Chinese yuan",
        "symbol": "CN¥",
        "symbol_native": "CN¥"
    },
    "connection": {
        "asn": 4134,
        "isp": "Chinanet"
    },
    "security": {
        "is_proxy": false,
        "proxy_type": null,
        "is_crawler": false,
        "crawler_name": null,
        "crawler_type": null,
        "is_tor": false,
        "threat_level": "low",
        "threat_types": null
    }
}
```

&emsp;

**地址⑤**：https://db-ip.com/demo/home.php?s=121.8.215.106 <a name="address-3.5"></a>

请求类型：GET

请求参数：s=你的ip

请求示例：

```
https://db-ip.com/demo/home.php?s=121.8.215.106
```

示例结果：

```
{
    "status": "ok",
    "demoInfo": {
        "ipAddress": "121.8.215.106",
        "continentCode": "AS",
        "continentName": "Asia",
        "countryCode": "CN",
        "countryName": "中国",
        "isEuMember": false,
        "currencyCode": "CNY",
        "currencyName": "Yuan Renminbi",
        "phonePrefix": "86",
        "languages": [
            "zh-CN",
            "yue",
            "wuu",
            "dta",
            "ug",
            "za"
        ],
        "stateProvCode": "GD",
        "stateProv": "广东",
        "district": "广州",
        "city": "小楼",
        "geonameId": 1790085,
        "latitude": 23.379,
        "longitude": 113.763,
        "gmtOffset": 8,
        "timeZone": "Asia/Shanghai",
        "weatherCode": "CHXX5497",
        "asNumber": 4134,
        "asName": "CHINANET-BACKBONE",
        "isp": "Chinanet",
        "usageType": "corporate",
        "organization": "Chinanet GD",
        "isCrawler": false,
        "isProxy": false,
        "threatLevel": "high",
        "threatDetails": [
            "attack-source",
            "attack-target:web"
        ]
    }
}
```

&emsp;

<a name="address-4.1"></a>

### 4.更多

1.只返回本机(访客)IP地址，通过curl访问测试 

- 请求类型：GET

```
curl ifconfig.me
curl ifconfig.es
curl icanhazip.com
curl ipinfo.io/ip
curl ipecho.net/ip
curl ident.me
curl eth0.me
curl ipaddr.site
curl ipaddress.sh
curl l2.io/ip
curl tnx.nl/ip
curl wgetip.com
curl ip.tyk.nu
curl curlmyip.net
curl ipcalf.com
curl checkip.amazonaws.com
```

示例结果：

```
121.8.215.106
```

&emsp;
