import requests
from bs4 import BeautifulSoup

def get_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    cookies = {
        "Cookie": "douban-fav-remind=1; ll='118099'; _vwo_uuid_v2=DF420B4CB23CA06454BECDF6BDAE779F8|4074cec7e02a4581ef62be030b2cc387; gr_user_id=8731d26b-4745-435c-8685-1aa854e49eb0; viewed='1451522_4212274_27152735'; bid=5W0AUBiViSU; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1602560567%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DAd5hH7ZcEyLg0fJR8yJvGzZxmvgMcXgkAJNV9uict41A-iRXQIBz8MaT08p4X7IY%26wd%3D%26eqid%3Dc99d4569000000a0000000025f852231%22%5D; _pk_id.100001.4cf6=59b372e229d2e816.1594046461.4.1602560567.1595520959.; _pk_ses.100001.4cf6=*; __utma=30149280.1377741326.1575034517.1602051736.1602560567.37; __utmc=30149280; __utmz=30149280.1602560567.37.36.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1160567393.1594046461.1595520953.1602560567.4; __utmb=223695111.0.10.1602560567; __utmc=223695111; __utmz=223695111.1602560567.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1602560567"
    }
    response = requests.get(url, headers=headers, cookies=cookies)

    if response.status_code == 200:     #爬取成功
        return response.text
    return None


for i in range(0,11):
    url = "https://movie.douban.com/subject/26885074/comments?start=" + str(20*i) + "&limit=20&status=P&sort=new_score"
    print("爬取第" + str(i+1) + "页")
    html = get_page(url)        #递归爬取

    soup = BeautifulSoup(html, 'html5lib')
    comments = soup.find(attrs={'class','mod-bd'})

    for item in comments.find_all(attrs={'class','short'}):
        print(item.string)