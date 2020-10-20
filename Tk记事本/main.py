import tkinter as Tk
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.messagebox
import tkinter.scrolledtext
import tkinter.simpledialog

# 文本编辑器
app=Tk.Tk()
app.title('NotePad')
app['width']=80
app['height']=80
textChanged=Tk.IntVar(app,value=0)      #当前内容是否发生改变
filename=''
menu=Tk.Menu()      #菜单

# File菜单
submenu=Tk.Menu(menu,tearoff=0)     #子菜单，是否可独立
def Open():
    global filename
    if textChanged.get():
        yesno=Tk.messagebox.askyesno(title='是否保存',
                                     message='是否保存？')
        if yesno==Tk.YES:
            Save()
    # 打开新文件（得到文件名）
    filename=Tk.filedialog.askopenfile(title='打开文件',
                                       filetypes=[('Text file','*.txt')])       #可打开文件类型
    if filename:
        txtContent.delete(0.0,Tk.END)       #清空（起始位置，截至位置）
        with open(filename,'r') as fp:      #读取文件内容，呈现在记事本上
            txtContent.insert(Tk.INSERT,''.join(fp.readlines()))
        textChanged.set(0)      #设置未修改
submenu.add_command(label='Open',command=Open)

def Save():
    global filename
    if not filename:        #没有文件名
        SaveAs()
    elif textChanged.get():
        with open(filename,'w') as fp:
            fp.write(txtContent.get(0.0,Tk.END))
        textChanged.set(0)
submenu.add_command(label='Save',command=Save)

def SaveAs():
    global filename
    newfilename=Tk.filedialog.asksaveasfilename(title='Save As',
                                                initialdir='.',
                                                initialfile='new.txt')
    if newfilename:
        with open(newfilename,'w') as fp:
            fp.write(txtContent.get(0.0,Tk.END))
        filename=newfilename
        textChanged.set(0)
submenu.add_command(label='Save As',command=SaveAs)

submenu.add_separator()     #分割线
def Close():
    global filename
    Save()
    txtContent.delete(0.0,Tk.END)
    filename=''     #清空文件名
submenu.add_command(label='Close',command=Close)
menu.add_cascade(label='File',menu=submenu)     #子菜单关联到主菜单

# Edit 菜单
submenu=Tk.Menu(menu,tearoff=0)
def Undo():     #撤销
    txtContent['undo']=True     #撤销标志
    try:
        txtContent.edit_undo()      #撤销
    except:
        pass
submenu.add_command(label='Undo',command=Undo)

def Redo():
    txtContent['undo']=True
    try:
        txtContent.edit_redo()
    except:
        pass
submenu.add_command(label='Redo',command=Redo)
submenu.add_separator()

def Copy():
    txtContent.clipboard_clear()        # 清空剪贴板
    txtContent.clipboard_append(txtContent.selection_get())     # 将选中的内容添加到剪贴板
submenu.add_command(label='Copy',command=Copy)

def Cut():
    txtContent.delete(Tk.SEL_FIRST,Tk.SEL_LAST)     #删除所选
submenu.add_command(label='Cut',command=Cut)

def Paste():
    try:                                            # 剪贴板
        txtContent.insert(Tk.SEL_FIRST,txtContent.clipboard_get())      #没有所选内容，直接粘贴到鼠标位置
        txtContent.delete(Tk.SEL_FIRST,Tk.SEL_LAST)     #删除再粘贴
        return
    except:
        pass
    txtContent.insert(Tk.INSERT,txtContent.clipboard_get())
submenu.add_command(label='Paste',command=Paste)
submenu.add_separator()

def Search():
    textToSearch=Tk.simpledialog.askstring(title='Search',
                                           prompt='搜索什么？')
    start=txtContent.search(textToSearch,0.0,Tk.END)
    if start:
        Tk.messagebox.showinfo(title='Found',message='OK')
submenu.add_command(label='Search',command=Search)
menu.add_cascade(label='Edit',menu=submenu)

# Help 菜单
submenu=Tk.Menu(menu,tearoff=0)
def About():
    Tk.messagebox.showinfo(title='About',message='Author:D')
submenu.add_command(label='About',command=About)
menu.add_cascade(label='Help',menu=submenu)

app.config(menu=menu)       #菜单添加到窗口

txtContent=Tk.scrolledtext.ScrolledText(app,wrap=Tk.WORD)       #内容与记事本关联
txtContent.pack(fill=Tk.BOTH,expand=Tk.YES)
def KeyPress(event):        #内容修改函数
    textChanged.set(1)
txtContent.bind('<KeyPress>',KeyPress)      #有键盘输入，则执行该函数表示修改过
app.mainloop()