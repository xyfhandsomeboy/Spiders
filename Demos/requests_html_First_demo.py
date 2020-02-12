from requests_html import HTMLSession

session = HTMLSession()
response = session.get("https://news.cnblogs.com/n/recommend")
file = open('LastBlog.txt', 'a+', encoding='utf-8')
for htmls in response.html:
    h2_s = htmls.find('h2')
    texts = htmls.find('.entry_summary')
    for h2, text in zip(h2_s, texts):
        title = h2.full_text
        link = h2.absolute_links.pop()
        print(link)
        print(type(link))
        print(type(title))
        print(title, text.full_text)
        file.write(title)
        file.write(text.full_text.strip() + '\n')
        file.write(link + '\n')
