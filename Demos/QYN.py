import re
import requests
from urllib.parse import urljoin

headers = {
    'Cookie': '_abcde_qweasd=0; _abcde_qweasd=0; bdshare_firstime=1578460431003; UM_distinctid=16fb896a4171b5-063181e4bdeca9-504f221b-1fa400-16fb896a418891; CNZZDATA1253551727=1118628257-1579346291-%7C1579346291; BAIDU_SSP_lcr=https://www.baidu.com/link?url=QZxDTzpe3XB2Q1_dvvQ4UxdpCiyBZohqsEU9nMFL1T7&wd=&eqid=c357d038002f7628000000065e230bd8; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1578492510,1578523933,1579315582,1579355102; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1579355110',
    'Host': 'www.xbiquge.la',
    'Referer': 'http://www.xbiquge.la/1/1690/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

number = 0
url = "http://www.xbiquge.la/1/1690/1267524.html"
while number <= 50:
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    html = r.text

    pattern_title = re.compile('<h1> (.*?)</h1>', re.S)
    pattern_content = re.compile('<div id="content">(.*?)</div>', re.S)
    pattern_lines = re.compile('\&nbsp;\&nbsp;\&nbsp;\&nbsp;(.*?)\\r<br />\\r<br />', re.S)
    pattern_next_url = re.compile('&rarr; <a href="(.*?)">下一章</a>', re.S)

    try:
        title = pattern_title.findall(html)
        contents = pattern_content.findall(html)
        lines = pattern_lines.findall(contents[0])
        next_url = pattern_next_url.findall(html)[0]

        url = urljoin(url, next_url)
        print(url)
        with open("庆余年\chapter-{}.txt".format(number), 'w') as f:
            f.write(title[0] + '\n')
            for line in lines:
                f.write(line + '\n')
                print(line)
        number += 1
    except:
        pass