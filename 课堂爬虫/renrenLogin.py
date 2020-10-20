import requests

session = requests.session()        #得到会话
post_url = "http://www.renren.com/PLogin.do"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}
post_data = {"email":"user13097679728", "password":"rrw123456"}     #输入账号密码
session.post(post_url, headers=headers, data=post_data)

url = "http://www.renren.com/975271170"     #获取信息页面（数字是登陆页面账号）
response = session.get(url, headers=headers)

with open("renren03.html","w",encoding="utf-8") as f:       #写入文件
    f.write(response.text)