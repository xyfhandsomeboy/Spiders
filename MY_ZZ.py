import re
import time
import requests
from urllib.parse import urljoin

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Cookie': '__mta=215440040.1579228594671.1579307391731.1579309410117.19; uuid_n_v=v1; uuid=2BE5A7A038D211EABDA9F528ED08AE1C55FBB8DFACB4456A856A33BE866650DC; _lxsdk_cuid=16fb15c019dc8-084905cbc5e9f3-504f221b-1fa400-16fb15c019ec8; _lxsdk=2BE5A7A038D211EABDA9F528ED08AE1C55FBB8DFACB4456A856A33BE866650DC; mojo-uuid=97f4fcd62363783fab8ad0d6d71cde82; _csrf=2611cfa76191f3e2dae45402053ed7ab11d0e179412c77fb445944b9d90c9f29; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1579228980,1579230844,1579305047,1579305511; __mta=215440040.1579228594671.1579305054654.1579305513089.15; mojo-session-id={"id":"567b648e3db50835386c0c5a67f66137","time":1579309409866}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1579309410; _lxsdk_s=16fb62d24f1-c54-d35-bc7%7C%7C3',
    'Host': 'maoyan.com',
    'Referer': 'https://maoyan.com/board'
}

num = 1
with open('Top100.txt', 'w', encoding='utf-8') as f:
    for number in range(0, 100, 10):
        # time.sleep(1)
        base_url = 'https://maoyan.com/board/4?offset={}'.format(number)
        r = requests.get(base_url, headers=header)
        r.encoding = r.apparent_encoding
        html = r.text

        film_url = re.compile('<p class="name">.*?<a href="(.*?)"', re.S)
        film_name = re.compile('<p class="name">.*?<a.*?title="(.*?)"', re.S)
        film_time = re.compile('<p class="releasetime">(.*?)</p>', re.S)
        file_sore = re.compile('<p class="score">.*?<i class="integer">(.*?)</i>.*?<i class="fraction">(.*?)</i>.*?</p>', re.S)

        urls = film_url.findall(html)
        names = film_name.findall(html)
        times = film_time.findall(html)
        sores = file_sore.findall(html)

        for url, name, time, sore in zip(urls, names, times, sores):
            # url = "https://www.maoyan.com" + url
            url = urljoin(base_url, url)
            final_sore = sore[0] + sore[1]
            f.write("No.{}  ".format(num))
            f.write("网址链接：" + url + "  ")
            f.write("电影：" + name + "  ")
            f.write(time + "  ")
            f.write("评分：" + final_sore + '\n')
            num += 1


