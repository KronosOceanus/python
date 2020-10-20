# 先全屏截图，再在全屏进行二次截图
import tkinter as tk
import tkinter.filedialog
import os
from PIL import ImageGrab
from time import sleep

root=tk.Tk()
root.geometry('100x40+400+300')
root.resizable(False,False)     # 不允许调整大小

class MyCapture:
    def __init__(self,png):
        self.x=tk.IntVar(value=0)
        self.y=tk.IntVar(value=0)
        # 屏幕尺寸
        sWidth=root.winfo_screenwidth()
        sHeight=root.winfo_screenheight()
        # 截屏时的顶级组件
        self.top=tk.Toplevel(root,width=sWidth,height=sHeight)
        # 不显示最大最小化
        self.top.overrideredirect(True)
        self.canvas=tk.Canvas(self.top,bg='white',width=sWidth,height=sHeight)
        # 显示全屏截图
        self.image=tk.PhotoImage(file=png)      # 转换为 tk 图像
        self.canvas.create_image(sWidth//2,sHeight//2,image=self.image)     # 图片中心位置

        def onLeftButtonDown(event):
            self.x.set(event.x)
            self.y.set(event.y)
            # 开始截图标志
            self.sel=True
        self.canvas.bind('<Button-1>',onLeftButtonDown)

        def onLeftButtonMove(event):
            if not self.sel:
                return
            global lastDraw
            try:
                # 删除刚画完的图形，不然移动过程中会有绘画
                self.canvas.delete(lastDraw)
            except:
                pass
            lastDraw=self.canvas.create_rectangle(self.x.get(),self.y.get(),
                                                  event.x,event.y,
                                                  outline='black')
        self.canvas.bind('<B1-Motion>',onLeftButtonMove)

        # 获取鼠标左键抬起位置，保存区域截图
        def onLeftButtonUp(event):
            self.sel=False
            try:
                self.canvas.delete(lastDraw)
            except:
                pass
            sleep(0.1)
            # 从右下到左上截图
            left,right=sorted([self.x.get(),event.x])
            bottom,top=sorted([self.y.get(),event.y])
            pic=ImageGrab.grab((left+1,bottom+1,right,top))
            # 保存截图对话框
            fileName=tk.filedialog.asksaveasfilename(title='保存截图',
                                                     filetypes=[('image','*.jpg *.png')])
            if fileName:
                pic.save(fileName)
            # 关闭当前窗口
            self.top.destroy()
        self.canvas.bind('<ButtonRelease-1>',onLeftButtonUp)
        self.canvas.pack(fill=tk.BOTH,expand=tk.YES)

# 开始截图
def buttonCaptureClick():
    # 最小化主窗口
    root.state('icon')
    sleep(0.2)

    filename='temp.png'
    im=ImageGrab.grab()     # 全屏截图
    im.save(filename)       # 暂存
    im.close()
    w=MyCapture(filename)       # 打开暂存，截图
    buttonCapture.wait_window(w.top)        # 等截图完毕，再接下来操作
    root.state('normal')        # 恢复主窗口
    os.remove(filename)     # 移除临时文件

# 截图按键
buttonCapture=tk.Button(root,text='截图',command=buttonCaptureClick)
buttonCapture.place(x=10,y=10,width=80,height=20)

root.mainloop()