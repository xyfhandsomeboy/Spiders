import csv
from urllib import robotparser
from urllib.parse import urlparse
from requests_html import HTMLSession

# 构造请求
session = HTMLSession()
url = "https://ai.baidu.com"
domain = urlparse(url).netloc
visited = []
unvisited = [url]

# 解析爬虫协议
rp = robotparser.RobotFileParser()
rp.set_url(url + '/robots.txt')
rp.read()

# 不访问的path
notpath = ('/file', '/docs', '/support', '/forum', '/broad', '/paddlepaddle', '/market',
           '/download', '/facekit', '/sdk', '/customer', '/easydl', '//')

def is_inner_link(link):
    netloc = urlparse(link).netloc
    return (not netloc) or (netloc == domain)

def add_judge(link):
    # 过滤1：爬虫协议是否允许
    allow = rp.can_fetch("*", link)
    if not allow:
        return

    # 过滤2：是否为内部链接
    if not is_inner_link(link):
        return

    # 过滤3：去掉非法链接
    path = urlparse(link).path
    if not path.startswith('/'):
        return

    # 过滤4：是否是需要访问的网址
    if path.startswith(notpath):
        return

    # 将/tech/123 转换为 https://ai.baidu.com/tech/123 的形式
    if link.startswith('/'):
        link = url + link

    # 过滤5：是否已经访问过
    if (link in visited) or (link in unvisited):
        return

    unvisited.append(link)

if __name__ == '__main__':
    file = open('BaiduiAI.csv', 'w', newline='', encoding='utf-8')
    csvwriter = csv.writer(file)
    csvwriter.writerow(['标题', '链接'])
    while unvisited:
        link = unvisited.pop()
        response = session.get(link)
        visited.append(link)
        if response.html and response.html.links and len(response.html.links):
             for href in response.html.links:
                 add_judge(href)

        if response.html.find('head title', first=True):
            csvwriter.writerow([response.html.find('head title', first=True).text, link])
            print(response.html.find('head title', first=True).text, link)
    file.close()

    print('一共爬取了{}个链接'.format(len(visited)))

