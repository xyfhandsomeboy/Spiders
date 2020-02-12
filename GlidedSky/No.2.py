from requests_html import HTMLSession
import requests


headers = {
    'Cookie': '_ga=GA1.2.1141903561.1581475469; _gid=GA1.2.266751034.1581475469; footprints=eyJpdiI6ImFVb2dveUFhSGhMQW0xdzFBQ3owOVE9PSIsInZhbHVlIjoidmpQVnRjR3UyWkhqTEJoVHZ1clNXbm1DMzd0QjJBUTJiYjVxSm8yeDM0cG50U2VNYlZzXC94Q0l6M1JXN21qeHYiLCJtYWMiOiJjZTkyMjQ1ODgzYjFkNzhiMWE1MmUwNWNhMzFjODJmMWI2OGUxNDcxZjZjMTNkNmM4YWQ1NzAyYWZmZmFiYzI1In0%3D; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1581475469,1581475505; XSRF-TOKEN=eyJpdiI6ImFzelhFWWMyZzl5bDdFM2tHRTBMcEE9PSIsInZhbHVlIjoiWXlTalwvVW03V2xzdDhkTE5yOExTTGlcL1pFMEQ4V0U1dklUekg1OHNJeEw0Wm5tS3UwSVNoUndtUnBqbkhJMmhoIiwibWFjIjoiZjBiOWI1NGU5NDM2ZGM1Y2FjYjgzN2E3MWFkZDg4M2QyMTE2ODQ2ZWE4OTJkOGYyYTMwODVkZjJiNjgyNjE5MSJ9; glidedsky_session=eyJpdiI6IlwvMm5YYW1mUkZicWFHdzh5dkZjMzF3PT0iLCJ2YWx1ZSI6IjBBaGt3QUpOejFvdE5IZW9kK2UxNXoxemorQ1o5N0dWZjVKbENwTHFHYnZubW80NTMwNDlDYWN6a1JvbVFsUXoiLCJtYWMiOiI1ZGFjZGJlYzZhMjIxMmUyNWExNzI0N2U0MzM4MjA5M2M3NmY5YjIyNjhmZDM5MDJhN2UyNzBmNDZkZWY5YjA5In0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1581479675',
    'Host': 'www.glidedsky.com',
    'Referer': 'http://www.glidedsky.com/level/web/crawler-basic-2?page=2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
sum = 0

session = HTMLSession()
url = "http://www.glidedsky.com/level/web/crawler-basic-2?page=1"
while True:
    response = session.get(url, headers=headers)
    divs = response.html.find('.row > div')
    for div in divs:
        num = int(div.text)
        print(num)
        sum += num
    try:
        url = response.html.find('.page-item:last-child a', first=True).attrs['href']
    except:
        break
print(sum)

