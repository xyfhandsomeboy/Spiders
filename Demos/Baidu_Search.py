from bs4 import BeautifulSoup
import requests
import re

headers = {
    'Cookie': 'BIDUPSID=1F234636F26E492C276F9067499CE0E0; PSTM=1578321167; BD_UPN=12314753; BAIDUID=5995BDDA2033533404DD240EC119147A:FG=1; BDUSS=jdoOERPUGMtVlZUfmJZUkJyZTFqLUxqMkg4YnhlZHVuUHJKRmFLcU0wTFRXME5lSVFBQUFBJCQAAAAAAAAAAAEAAAAo2~X4SEFORFNPTUVib3nR1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANPOG17Tzhteb; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; yjs_js_security_passport=f25ccbeb8347a355d6da0d6a60510b65566844c1_1580519514_js; H_PS_PSSID=1426_21091; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=6; cflag=13%3A3; BD_HOME=1; H_PS_645EC=9ee1Z7ESMUYCf4hqIM9KAX7LydrKUlZ7hFQxgFx%2Fsi5vXA8ROjogms74kpY',
    'Host': 'www.baidu.com',
    'Referer': 'https://www.baidu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

url = "https://www.baidu.com/s?ie=UTF-8&wd=%E5%86%9C%E6%9D%91%E4%BD%93%E9%AA%8C"
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
div_content = soup.find_all('div', id="content_left")[0]
# print(div_content)
h3_s = div_content.find_all(name='h3', class_="t")
div_s = div_content.find_all(name='div', class_="c-abstract")
# with open('entry.txt', 'a') as f:
for i, j in zip(h3_s, div_s):
    str1 = ""
    # f.write(i.get_text() + '\n')
    str1 = j.get_text()
    print(i.get_text())
    print(str1)
#     f.close()


# for i in div_s:
#     str1 = ""
#     # print(i)
#     str1 = i.get_text()
#     print(str1)