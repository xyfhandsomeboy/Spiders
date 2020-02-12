import requests
import csv
import json
import time as t

headers = {
    'Host': 'file1.dxycdn.com',
    'Referer': 'https://ncov.dxy.cn/ncovh5/view/pneumonia_timeline?whichFrom=dxy',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36'
}

url = "https://file1.dxycdn.com/2020/0130/492/3393874921745912795-115.json?t=26354134"
file = open('实时播报.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(file)
csv_writer.writerow(['标题', '摘要', '时间', '链接'])
response = requests.get(url, headers=headers)
data_json = json.loads(response.text)
data = data_json['data']
print(data)
for div in data:
    try:
        title = div['title']
        title = title.strip()
        summary = div['summary']
        summary = summary.strip()
        sourceURL = div['sourceUrl']
        time = div['pubDateStr']
        csv_writer.writerow([title, summary, time, sourceURL])
        print(title, summary, time, sourceURL)
        t.sleep(0.5)
    except:
        pass
file.close()
