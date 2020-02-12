from requests_html import HTMLSession
import requests
import time

# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "H87C7S0R00XU212D"
proxyPass = "F63A5047E72DC6F1"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

headers = {
    'Cookie': '_ga=GA1.2.1141903561.1581475469; _gid=GA1.2.266751034.1581475469; footprints=eyJpdiI6ImFVb2dveUFhSGhMQW0xdzFBQ3owOVE9PSIsInZhbHVlIjoidmpQVnRjR3UyWkhqTEJoVHZ1clNXbm1DMzd0QjJBUTJiYjVxSm8yeDM0cG50U2VNYlZzXC94Q0l6M1JXN21qeHYiLCJtYWMiOiJjZTkyMjQ1ODgzYjFkNzhiMWE1MmUwNWNhMzFjODJmMWI2OGUxNDcxZjZjMTNkNmM4YWQ1NzAyYWZmZmFiYzI1In0%3D; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1581475469,1581475505; XSRF-TOKEN=eyJpdiI6IlwvaXBkV2Z6QjdGMEl1YjVGSlcxTTVnPT0iLCJ2YWx1ZSI6ImNKNU93S2lUNkNFY0NuRG9BZXo3clF5ZnQyeWd0OWxnNVZCRzFKalRKOHZVUEluSzVLaEpDZWVuNVJNMFNoVU0iLCJtYWMiOiJlNjQxYjFlZDJiYTAxYzViMjBlYTFjZTA2YWVkNDM4YjdhMjc0M2UyODdlZWFkOTMwYTYzOTM5OTNjZDBkODZmIn0%3D; glidedsky_session=eyJpdiI6ImIrU2JIRDYrcWV6WHRTbjRLRjBwS2c9PSIsInZhbHVlIjoiUkc5Wk1TWFVEQURDaW9GcFwvb212T093cTJ1VzFkVlZ2RXRhWngwcWdKcUFIdUZMWlNcLzdEVGg3Z2hBOUJmck5SIiwibWFjIjoiNzZiYzRjNmVjODdiYjUxMDczZGMwZTllNDkxNDUyNTMzMDFhMzE4NmY4ZDdiMzczM2NiNjNmZTM4OThlOTdlMyJ9; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1581486119; _gat_gtag_UA_75859356_3=1',
    'Host': 'www.glidedsky.com',
    'Referer': 'http://www.glidedsky.com/level/crawler-ip-block-1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
sum = 0
i = 1
session = HTMLSession()
while i <= 1000:
    url = "http://www.glidedsky.com/level/web/crawler-ip-block-1?page={}".format(i)
    print(url)
    try:
        response = session.get(url, headers=headers, proxies=proxies)
        divs = response.html.find('.row > div')
        if divs != []:
            for div in divs:
                num = int(div.text)
                print(num, end=' ')
                sum += num
            print("请求成功")
            i += 1
    except:
        print("请求失败")
        pass
    finally:
        time.sleep(0.3)
print(sum)

# 2515865