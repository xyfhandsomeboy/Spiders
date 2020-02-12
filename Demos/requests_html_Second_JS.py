from apscheduler.schedulers.blocking import BlockingScheduler
from requests_html import HTMLSession
from datetime import datetime
from wordcloud import WordCloud
import requests
import jieba
import time
import re

def get_Baidu_news_title():
    url = "https://news.baidu.com/"
    session = HTMLSession()
    response = session.get(url)
    Baidu_news_title = []
    # 如果后面加了first=True这种字样，那么返回的就是一个标签而不是标签列表
    total_title = response.html.find('.hdline0 a', first=True)
    Baidu_news_title.append(total_title)
    # print(Baidu_news_title)
    titles = response.html.find('#pane-news > ul .bold-item a')
    Baidu_news_title += titles
    # print(Baidu_news_title)
    with open('news_titles.txt', 'w', encoding='utf-8') as f:
        for title in Baidu_news_title:
            f.write(title.text + '\n')
            # print(title.text)
        f.close()

# 爬出来的数据为乱码，故舍弃
def get_WangYi_news_title():
    url = "https://news.163.com/"
    session = HTMLSession()
    response = session.get(url)
    response.html.render()
    print(response.html.text)
    div = response.html.find('.mod_top_news2', first=True)
    text = div.full_text
    with open('news_titles.txt', 'w', encoding='utf-8') as f:
        f.write(text)
        f.close()

if __name__ == '__main__':
    # 定时运行程序
    # sched = BlockingScheduler()
    # sched.add_job(get_Baidu_news_title, 'cron', hour=9, minute=59)
    # sched.start()
    get_Baidu_news_title()
    text = ""
    with open('news_titles.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        f.close()
    seg_list = jieba.cut(text, cut_all=True)
    # print(seg_list)
    word_split = " ".join(seg_list)
    print(word_split)
    my_wordcloud = WordCloud(background_color='white', font_path='C:\Windows\Fonts\SIMLI.TTF',
                             max_words=10, width=1600, height=800)
    my_wordcloud= my_wordcloud.generate(word_split)
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    my_wordcloud.to_file(now + '.png')


# split 是根据什么分割开来，而join是把一个列表（全是字符串）拼接在一起，并且.join前面的是连接符