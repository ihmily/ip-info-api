# ip-info-api

该存储库收集了各种免费的IP查询API，使开发人员能够快速访问IP信息，如地理位置、ISP详细信息和网络类型。持续更新中，欢迎star

### IP地址

1.可查询本机IP和通过IP查询

[https://webapi-pc.meitu.com/common/ip_location](#address-1.1) 

[https://www.ip.cn/api/index?ip=&type=0](#address-1.2) 

[https://whois.pconline.com.cn/ipJson.jsp?ip=&json=true](#address-1.3) 

[https://api.vore.top/api/IPdata?ip=](#address-1.4) 

2.只可查询本机IP

[https://ip.useragentinfo.com/json](#address-2.1) 

[http://httpbin.org/ip](#address-2.2) 

[https://cdid.c-ctrip.com/model-poc2/h](#address-2.3) 

3.只可通过IP查询

[http://opendata.baidu.com/api.php?co=&resource_id=6006&oe=utf8&query=](#address-3.1) 

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
<a name="address-2.1"></a>
### 2.只可查本机IP 

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

