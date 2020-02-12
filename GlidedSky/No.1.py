from requests_html import HTMLSession
import requests

headers = {
    'Cookie': '_ga=GA1.2.1141903561.1581475469; _gid=GA1.2.266751034.1581475469; footprints=eyJpdiI6ImFVb2dveUFhSGhMQW0xdzFBQ3owOVE9PSIsInZhbHVlIjoidmpQVnRjR3UyWkhqTEJoVHZ1clNXbm1DMzd0QjJBUTJiYjVxSm8yeDM0cG50U2VNYlZzXC94Q0l6M1JXN21qeHYiLCJtYWMiOiJjZTkyMjQ1ODgzYjFkNzhiMWE1MmUwNWNhMzFjODJmMWI2OGUxNDcxZjZjMTNkNmM4YWQ1NzAyYWZmZmFiYzI1In0%3D; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1581475469,1581475505; XSRF-TOKEN=eyJpdiI6InFQajErRmtIS2t0cnFmTXZPNXN6T0E9PSIsInZhbHVlIjoidU15QU9vcnNSTlAxWFlCOUJhbk4ydElqY0ttNEZpUUFBc1p5XC9HeGhORFZQdjBsQ0JIY1wvbDJzRGh1V3BBSDNIIiwibWFjIjoiOWIyNTUxN2M3MjEzOWE4ZGJiNWIxMDNjYTc2YTI0Zjc5OWNhNDgzNWNhYWMzYTg4Y2RlN2M2ZjZkZTI5ZWVhNCJ9; glidedsky_session=eyJpdiI6IlhaZ1NubTh1S1wvaEZaeHV6NnlIVmxBPT0iLCJ2YWx1ZSI6Ik5NWVBhVUQ1S2R1RmNnUzBBN20xMkhKd3NvcnBFN01TUlpHUm55SStVZnBDRUhCcllcLzQ2TEtXUVFSR2JwZ29iIiwibWFjIjoiZWJjMzVjNmZhZDY2ZTkxNDRhMWE3YzkyMGYxNTMxZTg1ZGNkNDkyM2M2NjZjYjdjN2U4NjllNWE5ZjgxNmJiMCJ9; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1581478011; _gat_gtag_UA_75859356_3=1',
    'Host': 'www.glidedsky.com',
    'Referer': 'http://www.glidedsky.com/level/crawler-basic-1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}

session = HTMLSession()
url = "http://www.glidedsky.com/level/web/crawler-basic-1"
response = session.get(url, headers=headers)
divs = response.html.find('.row > div')
sum = 0
for div in divs:
    num = div.text
    print(num)
    sum += int(num)
print(sum)