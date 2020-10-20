'''failed'''
import os
import urllib.request
import scrapy

class MySpider(scrapy.spiders.Spider):
    name='mySpider'     # 爬虫名称（*）
    allowed_domains=['ww.dibt.edu.cn']
    start_urls=['http//ww.dibt.edu.cn/info/1026/11238.htm']     # 要爬取的初始页面（可多个）

    def parse(self, response):
        self.downloadWebpage(response)
        self.downloadImages(response)

        hxs=scrapy.Selector(response)       # 检查页面中超链接，并继续爬取
        sites=hxs.xpath('//ul/li')
        for site in sites:
            link=site.xpath('a/@href').extract()[0]
            if link=='#':
                continue
            elif link.startswith('..'):      # 把相对地址转化成绝对地址
                next_url=os.path.dirname(response.url)
                next_url+='/'+link
            else:
                next_url=link
            yield scrapy.Request(url=next_url,callable=self.parse_item)

    # 回调函数，对起始页面中每个超链接起作用
    def parse_item(self,response):
        hxs=scrapy.Selector(response)
        images=hxs.xpath('//img/@src').extract()
        for image_url in images:
            imageFilename=image_url.split('/')[-1]
            if os.path.exists(imageFilename):
                continue
            if image_url.startswith('..'):
                image_url=os.path.dirname(response.url)+'/'+image_url
            fp=urllib.request.urlopen(image_url)
            with open(imageFilename,'wb') as f:
                f.write(fp.read())
            fp.close()

    # 把网页内容保存为本地文件
    def downloadWebpage(self,response):
        filename=response.url.split('/')[-1]
        with open(filename,'wb') as f:
            f.write(response.body)