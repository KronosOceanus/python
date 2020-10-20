import lxml.html,requests

url = 'https://www.python.org/dev/peps/pep-0020/'
xpath = '// * [@id = "the-zen-of-python"]/pre/text()'   # 根据 xpath 定位
res = requests.get(url)     # 得到 Response 对象
ht = lxml.html.fromstring(res.text)     # 读取请求文本内容，得到 htmlElement
text = ht.xpath(xpath)      # 根据定位得到内容
print('Hello,\n' + ''.join(text))       # 循环输出
