import csv

page_url = []
page_title = []
file = open('BaiduiAI.csv', 'r', encoding='utf-8')
infos = csv.reader(file)
for info in infos:
    page_title.append(info[0])
    page_url.append(info[1])

while True:
    keyword = input("请输入查询关键字，输入 quit 结束：")
    if keyword == 'quit':
        break
    for i in range(len(page_title)):
        if page_title[i].find(keyword) >= 0:
            print(page_url[i], page_title[i])


