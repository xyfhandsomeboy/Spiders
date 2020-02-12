from requests_html import HTMLSession
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import json
import csv
import re

headers = {
    'Cookie': 'bid=QlgG326Fc-I; ll="118211"; __utmz=30149280.1580807744.1.1.utmcsr=python123.io|utmccn=(referral)|utmcmd=referral|utmcct=/tutorials/web_crawler/index.html; __utmz=223695111.1580807744.1.1.utmcsr=python123.io|utmccn=(referral)|utmcmd=referral|utmcct=/tutorials/web_crawler/index.html; __gads=ID=9ee63b165a59a666:T=1580807744:S=ALNI_MYBJIFHf3Syzabtb3fJGMdKwvZ6vw; __yadk_uid=DiQxgIPLTGQ1OzOdczyvsegO7oaL3O7o; _vwo_uuid_v2=DBC3A8950716F98CD1044756BA0F2FEE9|fd7ba5f88b8ece0278550e002d802071; __utmc=30149280; __utmc=223695111; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1581400027%2C%22https%3A%2F%2Fpython123.io%2Ftutorials%2Fweb_crawler%2Findex.html%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1322189123.1580807744.1581394651.1581400027.3; __utmb=30149280.0.10.1581400027; __utma=223695111.1355415709.1580807744.1581394651.1581400027.3; __utmb=223695111.0.10.1581400027; _pk_id.100001.4cf6=d197477eed097290.1580807744.3.1581400099.1581394651.',
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
films_response = requests.get(url, headers=headers)
session = HTMLSession()

def find_comments_url(film_url):
    response = session.get(film_url)
    comments_url = response.html.find('.mod-hd > h2 a', first=True).attrs['href']
    return comments_url


def parse_comments(title, comments_url):
    r = session.get(comments_url)
    divs = r.html.find('.mod-bd > div.comment-item')
    file = open('{}.csv'.format(title), 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow(['用户名称', '评论'])
    for div in divs:
        username = div.find('h3 span.comment-info a', first=True).text
        comments = div.find('p span', first=True).text
        print(username, comments)
        csv_writer.writerow([username, comments])
    file.close()


if __name__ == '__main__':
    films_json = json.loads(films_response.text)
    films = films_json['subjects']
    comments_url = ""
    i = 0
    for film in films:
        if i == 3:
            break
        title = film['title']
        film_url = film['url']
        print(title, film_url)
        comments_url = find_comments_url(film_url)
        parse_comments(title, comments_url)
        i += 1

