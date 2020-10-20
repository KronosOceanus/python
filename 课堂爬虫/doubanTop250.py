from pyquery import PyQuery as pq
import requests

def get_page(pages):
    url = "https://movie.douban.com/top250"
    pages *= 25
    params = {
        "start":pages,
        "filter":""
    }
    headers = {
        "Host":"movie.douban.com",
        "User-Agent":"Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.181Safari / 537.36"
    }
    try:
        res = requests.get(url, params=params, headers=headers)
        if res.status_code == 200:
            return res.text
    except requests.exceptions as e:
        print("Error:",e.args)

def parser_page(html, num):
    doc = pq(html)
    movies = doc(".grid_views .info").items()       #无法遍历
    for position, movie in enumerate(movies, start=1 + num*25):     #设置起始位置（元组）
        name = movie(".hd a span").text().strip(" ")
        detail = movie(".bd p").text()
        actor = detail.split("\n")[0]
        times = detail.split("\n")[1]
        rating = movie(".star .rating_num").text().strip(" ")
        print("------------------", position, "------------------")
        print("电影名称：",name, "\n",
              "导演和主演：", actor, "\n",
              "上映时间/地区：", times, "\n"
              "评分：", rating, "\n")

for num in range(10):
    html = get_page(num)
    parser_page(html, num)