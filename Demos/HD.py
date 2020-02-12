import re
import requests
from urllib.parse import urljoin

url = "http://www.hlju.edu.cn/"
r = requests.get(url)
r.encoding = r.apparent_encoding
news = re.compile('<td valign="middle" align="left">.*?<a href="(.*?htm)" class="c113092" title="(.*?)" target="_blank">', re.S)
results = news.findall(r.text)
for result in results:
    news_url = urljoin(url, result[0])
    print(news_url, result[1])