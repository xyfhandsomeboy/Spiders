import urllib.robotparser

url = "https://ai.baidu.com"
rp = urllib.robotparser.RobotFileParser()
rp.set_url(url + '/robots.txt')
rp.read()
# 第一个参数是用户类型。此处为*说明是任意用户，第二个参数是网址
info = rp.can_fetch("*", 'https://ai.baidu.com/tech/s peech/asr')
print(info)