import urllib.robotparser as urobot
import requests

url="https://www.taobao.com/"
rp=urobot.RobotFileParser()
rp.set_url(url + "/robots.txt")     # 爬虫协议文件
rp.read()
user_agent='Baiduspider'
if rp.can_fetch(user_agent, 'https://www.taobao.com/article'):      # 判断是否能爬取
    site=requests.get(url)      # 得到相应
    print('seems good')
else:
    print('failed')