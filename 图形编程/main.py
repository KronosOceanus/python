from PIL import Image
im=Image.open('sample.jpg')
# im.show()

print(im.format)
print(im.size)
print(im.height)

print(im.histogram())       #通道直方图
print(im.getpixel((150,80)))        #读取坐标像素（三原色）
im.putpixel((150,80),(128,30,120))      #修改像素
im.putpixel((150,80),(2, 34, 75))

# im.save('sample.jpg')       #另存为
# im.save('samplee.bmp')      #格式转换

def img2jpg(imgFile):
    '''转换图片格式'''
    if type(imgFile)==str and imgFile.endswith(('.bmp','.gif','.png')):
        with Image.open(imgFile) as im:
            # convert 指定色彩模式
            im.convert('RGB').save(imgFile[:-3]+'jpg')
# img2jpg('samplee.bmp')

im=im.resize((1280,903))     #图像缩放
im=im.rotate(90)        #逆时针旋转 90
im=im.transpose(Image.ROTATE_180)       #逆 180
im=im.transpose(Image.FLIP_LEFT_RIGHT)      #水平翻转
im=im.transpose(Image.FLIP_TOP_BOTTOM)      #垂直翻转

box=(120,194,220,294)       #裁剪区域
region=im.crop(box)
region=region.transpose(Image.ROTATE_180)
im.paste(region,box)        #粘贴

r,g,b=im.split()        #三原色分图
imNew=Image.merge(im.mode,(r,g,b))      #合成

im.thumbnail((40,28),Image.ANTIALIAS)       #缩略图
# im.save('2.jpg')

from PIL import ImageGrab
im=ImageGrab.grab((0,0,800,200))      #截图
im=ImageGrab.grab()     #全屏截图

from PIL import ImageFilter     #图像增强
im=im.filter(ImageFilter.DETAIL)        #滤波器
im=im.filter(ImageFilter.EDGE_ENHANCE)      #边缘增强
im=im.filter(ImageFilter.EDGE_ENHANCE_MORE)      #边缘增强

im=im.filter(ImageFilter.BLUR)      #模糊
im=im.filter(ImageFilter.GaussianBlur)      #高斯模糊
im.filter(ImageFilter.MedianFilter)     #中值滤波

# im=im.filter(ImageFilter.FIND_EDGES)        #边缘提取
im=im.point(lambda i:i*1.3)     #整体变亮（>1）
im=im.point(lambda i:i*0.7)

from PIL import ImageEnhance
enh=ImageEnhance.Brightness(im)     #亮
# enh.enhance(1.3).show()

r,g,b=im.split()        #冷暖调整
r=r.point(lambda i:i*1.3)
g=g.point(lambda i:i*0.9)
b=b.point(lambda i:0)
im=Image.merge(im.mode,(r,g,b))

im=ImageEnhance.Contrast(im)
im=im.enhance(1.3)      #对比度增强