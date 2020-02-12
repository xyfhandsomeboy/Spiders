from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://python.org')
print(r.html.absolute_links)
about = r.html.find('#about', first=True)
print(about.html)
print(about.search_all('li'))
print(type(about.text))