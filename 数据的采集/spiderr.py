import pymysql.cursors
import requests
from bs4 import BeautifulSoup
import arrow

urls = [        # {} 是 format 占位符，pn 参数表示翻页
    u'https://news.so.com/ns?q=%E5%8C%97%E4%BA%AC&pn={}&tn=newstitle&rank=rank&j=0&nso=10&tp=11&nc=0&src=page'
        .format(i) for i in range(10)
]
for i,url in enumerate(urls):
    r = requests.get(url)
    bs1 = BeautifulSoup(r.text, "html.parser")
    items = bs1.find_all('a', class_='news_title')

    t_list = []
    for one in items:
        t_item = []
        if '360' in one.get('href'):        #除去其他超链接
            continue
        t_item.append(one.get('href'))      #超链接
        t_item.append(one.text)     #文本
        date = [one.next_sibling][0].find('span',class_='pdate').text       #在超链接结点之后一个结点中寻找 span（时间/多久前）
        if len(date) < 6:
            date = arrow.now().shift(days = -int(date[:1])).date()
        else:
            date = arrow.get(date[:10],'YYYY-MM-DD').date()

        t_item.append(date)
        t_list.append(t_item)