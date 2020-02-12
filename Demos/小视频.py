from requests_html import HTMLSession
from urllib.parse import urljoin
import requests

def parseHtml(href, title):
    session = HTMLSession()
    response = session.get(href)
    response.html.render()
    div = response.html.find('#my-video_html5_api', first=True)
    print(div.attrs['src'])
    video_url = div.attrs['src']
    r = requests.get(video_url).content
    with open('./Video/{}.mp4'.format(title), 'wb') as file:
        file.write(r)
        print('写入成功')
    file.close()

url = "https://www.ku6.com/index"
s = HTMLSession()
r = s.get(url)
a_s = r.html.find('div#video-container > div > div h3 > a')
print(a_s)
i = 0
for a in a_s:
    print(a)
    if i == 5:
        break
    href = a.attrs['href']
    title = a.text
    href = urljoin(url, href)
    print(title, href)
    parseHtml(href, title)
    i += 1

