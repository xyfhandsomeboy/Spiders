from requests_html import HTMLSession
import requests

def Save_img(title, src):
    img_response = requests.get(src)
    with open('./BackGroud/' + title + ".jpg", 'wb') as f:
        print(title, src)
        f.write(img_response.content)
        print("保存成功")

url = "http://www.win4000.com/wallpaper_2358_0_10_1.html"
session = HTMLSession()
response = session.get(url)
for html in response.html:
    img_items = html.find('ul.clearfix > li > a')
    for img in img_items:
        href =img.attrs['href']
        if "/wallpaper_detail" in href:
            r = session.get(href)
            src = r.html.find('img.pic-large', first=True).attrs['src']
            title = r.html.find('img.pic-large', first=True).attrs['title']
            Save_img(title, src)
