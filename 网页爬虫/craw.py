import re
import os
import urllib.request as lib

def craw_links(url, depth, keywords, processed):
    '''要爬取的 url
        当前抓取深度
        聚焦的关键词
        爬取的所有网站过程'''
    contents=[]
    if url.startswith(('http://','https://')):
        if url not in processed:
            processed.append(url)
        else:
            return

        print('正在爬取：'+url)
        fp=lib.urlopen(url)
        contents=fp.read()      # 读取 html
        contens_decoded=contents.decode('UTF-8')
        fp.close()

        pattern='|'.join(keywords)      # 匹配关键字
        flag=False
        if pattern:
            searched=re.search(pattern,contens_decoded)
        else:
            flag=True
        if flag or searched:
            with open('craw\\'+url.replace(':','_').replace('/','_'),'wb') as fp:    # 写入文件名
                fp.write(contents)

        links=re.findall('href="(.*?)"',contens_decoded)        # 匹配超链接
        for link in links:
            if not link.startswith(('http://','https://')):
                try:
                    index=url.rindex('/')       # 相对路径拼接 url
                    link=url[0:index+1]+link
                except:
                    pass

            if depth>0 and link.endswith(('.htm','.html')):         # 递归爬取
                craw_links(link,depth-1,keywords,processed)

if __name__ == '__main__':
    processed=[]
    keywords=('datetime','KeyWord2')
    if not os.path.exists('craw') or not os.path.isdir('craw'):
        os.mkdir('craw')
    craw_links(r'https://docs.python.org/3/library/index.html',1,keywords,processed)