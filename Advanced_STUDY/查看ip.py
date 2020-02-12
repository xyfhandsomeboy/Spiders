import requests

# # 代理服务器
# proxyHost = "http-dyn.abuyun.com"
# proxyPort = "9020"
#
# # 代理隧道验证信息
# proxyUser = "H4L79387A9R6H5GD"
# proxyPass = "31A4FB307F892915"
#
# proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
#     "host": proxyHost,
#     "port": proxyPort,
#     "user": proxyUser,
#     "pass": proxyPass,
# }
#
# proxies = {
#     "http": proxyMeta,
#     "https": proxyMeta,
# }

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}
url = 'http://icanhazip.com/'
response = requests.get(url, headers=headers)
ip = response.text.replace('\n', '')
print(ip)
