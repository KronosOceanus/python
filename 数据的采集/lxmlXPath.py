from lxml import etree
from lxml import html
import requests

doc = etree.parse("applicationContext.xml")     #解析 XML 并建立树状结构
print(doc)

text = requests.get("https://www.baidu.com").text
print(text)
ht = html.fromstring(text)       #建立树状结构
htEle = ht.xpath('//*[@type="hidden"]')[0]
print(htEle.text)       #标签的文本
print(htEle.attrib)     #属性（dict）
print(htEle.get("class"))       #根据属性名获取属性
print(htEle.keys())     #所有属性名
print(htEle.values())       #所有属性值

print()
#与上面语句等效的 xpath 语句
print(ht.xpath('//*[@id="wrapper"]')[0].xpath('./@id')[0])
print(ht.xpath('//*[@id="wrapper"]')[0].xpath('./text()')[0])

print(ht.xpath('//*[@id="wrapper"][position()=1]/text()'))
print(ht.xpath('//*[@id="wrapper"][position()=1]/@lang'))

#过滤 script 与 style 标签之间（影响解析）的内容
from lxml.html import clean
cleaner = clean.Cleaner(style=True, scripts=True,page_structure=False,safe_attrs_only=False)
h1clean = cleaner.clean_html(text.strip())
print(h1clean)