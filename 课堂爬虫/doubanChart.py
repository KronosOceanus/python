from lxml import etree
import requests

url = "https://movie.douban.com/chart"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}
res = requests.get(url, headers=headers)
html_str = res.content.decode()
html = etree.HTML(html_str)

url_list = html.xpath("//div[@class='indent']/div/table//div[@class='pl2']/a/@href")
img_list = html.xpath("//div[@class='indent']/div/table//a[@class='nbg']/img/@src")
ret1 = html.xpath("//div[@class='indent']/div/table")
for table in ret1:
    item = {}
    item["title"] = table.xpath(".//div[@class='pl2']/a/text()")[0].replace("/","")
    item["href"] = table.xpath(".//div[@class='pl2']/a/@href")[0]
    item["img"] = table.xpath(".//a[@class='nbg']/img/@src")[0]
    item["comment_num"] = table.xpath(".//span[@class='pl']/text()")[0]
    item["rating_num"] = table.xpath(".//span[@class='rating_nums']/text()")[0]
    print(item)