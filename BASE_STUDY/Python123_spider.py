from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://movie.douban.com/subject/1292052/')
print(r.text)