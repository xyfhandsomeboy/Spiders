from requests_html import HTMLSession
from lxml import etree
import requests
import csv
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36'
}

url = "https://music.163.com/discover/toplist"
base_url = "https://link.hhtjim.com/163/"
response = requests.get(url, headers=headers)
html = etree.HTML(response.text, etree.HTMLParser())
ids = html.xpath('//a[contains(@href, "/song?")]/@href')
for id in ids:
    if ('$' in id) is False:
        id = id.strip('/song?id=')
        href = base_url + id + '.mp3'
        print(href)
