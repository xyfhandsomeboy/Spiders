import re
import time
import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'mta=188560663.1578990190789.1578990194464.1578990198891.3; uuid_n_v=v1; uuid=18FBB99036A711EABA7A9D25047E3BAECF0CA7112DAC4173B0E0492F8EEB440A; _csrf=3323d8d90b0ff446cbf433ba6c82e6b18a68f23772dd497ff279f4816664987d; mojo-uuid=dfbd08a91efa090758069b8db74a0f8c; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1578990191; mojo-session-id={"id":"1e6eccea0d2ad4fa9fddfa18f653fa88","time":1578990190679}; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=16fa32640a1c8-0fd0c9238d1dca-1a201708-151800-16fa32640a1c8; _lxsdk=18FBB99036A711EABA7A9D25047E3BAECF0CA7112DAC4173B0E0492F8EEB440A; __mta=188560663.1578990190789.1578990190789.1578990194464.2; mojo-trace-id=5; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1578990199; _lxsdk_s=16fa32640a2-d3-e16-558%7C%7C8',
    'Host': 'maoyan.com',
    'Referer': 'https://maoyan.com/board',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
number = 0
rank = 1
with open('../top_100_film_zz.txt', 'w') as f:
    for number in range(0, 100, 10):
        time.sleep(1)
        url = "https://maoyan.com/board/4?offset={}".format(number)
        r = requests.get(url, headers=headers)
        r.encoding = r.apparent_encoding
        div = r.text
        div = str(div)
        film_name = re.compile('<p class="name">.*?title="(.*?)"', re.S)
        film_stars = re.compile('<p class="star">\n(.*?)</p>', re.S)
        film_sore = re.compile('<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>', re.S)
        names = film_name.findall(div)
        stars = film_stars.findall(div)
        sores = film_sore.findall(div)
        for name, star, sore in zip(names, stars, sores):
            s = ''
            star = star.strip()
            f.write('No.{}:'.format(rank))
            f.write(name + ',')
            f.write(star + ',')
            for i in sore:
                s += i
            f.write('sore:' + s)
            f.write('\n')
            rank += 1
        print(names)
        print(stars)
        print(sores)