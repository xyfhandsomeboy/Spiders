from requests_html import HTMLSession
import requests
import re

url = "https://www.pearvideo.com/video_1650586"
r = requests.get(url)
pattern = re.compile('srcUrl="(.*?).mp4"', re.S)
film_url = pattern.findall(r.text)[0] + '.mp4'
print(film_url)