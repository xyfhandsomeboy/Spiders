from requests_html import HTMLSession
import requests
import csv
import re

headers = {
    'cookie': 'lastCity=101010100; _uab_collina=157957561676873243289516; __c=1581155077; __g=-; __l=l=https%3A%2F%2Fwww.google.com%2F&r=https%3A%2F%2Fwww.google.com%2F&friend_source=0&friend_source=0; __zp_seo_uuid__=26d311de-c53f-46bf-bbc2-47b355ce07e8; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1579575617,1580553217,1581155077,1581161389; toUrl=https%3A%2F%2Fwww.zhipin.com%2F%2Fjob_detail%2Fb8dfdb840a7788a60nB72du1GVo%7E.html; JSESSIONID=""; __a=99882289.1579575617.1580553217.1581155077.21.3.14.21; __zp_stoken__=af72hthJpuw8GASR5Y9U5AYobqkJr0kCXzDqiTk34JLRvyByZGTgVDf37DVyeECAPnMKq5X%2Bs%2FCH6lfOrK114g0M9fosC0OJLX6bqF4Kyr7KUhungX%2FRWTi1AHMCs2kAJl%2BB; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1581163185',
    'referer': 'https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position=',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36'
}
session = HTMLSession()
url = "https://www.zhipin.com/job_detail/?query=python%E7%88%AC%E8%99%AB%E5%B7%A5%E7%A8%8B%E5%B8%88&city=101010100&industry=&position="
response = session.get(url)
print(response.html.html)
print(response.html.links)
# response.html.render(sleep=3)
lis = response.html.find('.job-list ul > li')
print(lis)
# file = open('boss.csv', 'w', newline='')
# csv_writer = csv.writer(file)
# csv_writer.writerow(['工作名', '工作地区', '工作薪资'])
# for li in lis:
#     job_name = li.find('span.job-name', first=True).text
#     job_area = li.find('span.job-area', first=True).text
#     job_salary = li.find('span.red', first=True).text
#     print(job_name)
#     print(job_area)
#     print(job_salary)
#     csv_writer.writerow([job_name, job_area, job_salary])
# file.close()