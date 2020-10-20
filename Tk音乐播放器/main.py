import os
import tkinter as tk
import tkinter.filedialog
import random
import time
import threading
import pygame

folder=''

def play():
    # 默认播放文件夹内文件
    global folder
    musics=[folder+'\\'+music for music in os.listdir(folder)\
            if music.endswith('.mp3')]
    # 初始化混音设备
    pygame.mixer.init()
    while playing:
        # 未播放
        if not pygame.mixer.music.get_busy():
            # 随机播放
            nextMusic=random.choice(musics)
            pygame.mixer.music.load(nextMusic.encode())     # 编码
            # 播放一次
            pygame.mixer.music.play(1)
            musicName.set('playing...'+nextMusic)
        else:
            time.sleep(0.3)     # 0.3s 检测一次

root=tk.Tk()
root.title('音乐播放器')
root.geometry('280x70+400+300')
root.resizable(False,False)

# 关闭窗口（关闭音乐）
def closeWindow():
    global playing
    playing=False
    try:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    except:
        pass
    root.destroy()
root.protocol('WM_DELETE_WINDOW',closeWindow)       # 窗口点击事件绑定

pause_resume=tk.StringVar(root,value='NotSet')      # 暂停按钮状态
playing=False

# 播放
def buttonPlayClick():
    global folder
    if not folder:
        folder=tk.filedialog.askdirectory()     # 选定文件夹
    if not folder:
        return
    # 播放
    global playing
    playing=True
    t=threading.Thread(target=play)     # 以函数创建线程
    t.start()
    # 设置可用按钮
    buttonPlay['state']='disabled'
    buttonStop['state']='normal'
    buttonPause['state']='normal'
    buttonNext['state']='normal'
    pause_resume.set('Pause')
buttonPlay=tk.Button(root,text='play',command=buttonPlayClick)      # 播放按钮
buttonPlay.place(x=20,y=10,width=50,height=20)

# 停止
def buttonStopClick():
    global playing
    playing=False
    pygame.mixer.music.stop()
    musicName.set('None')
    buttonPlay['state']='normal'
    buttonStop['state']='disabled'
    buttonPause['state']='disabled'
buttonStop=tk.Button(root,text='Stop',command=buttonStopClick)
buttonStop.place(x=80,y=10,width=50,height=20)
buttonStop['state']='disabled'

# 暂停
def buttonPauseClick():
    global playing
    if pause_resume.get()=='Pause':
        pygame.mixer.music.pause()
        pause_resume.set('Resume')
    elif pause_resume.get()=='Resume':
        pygame.mixer.music.unpause()        # 继续播放
        pause_resume.set('Pause')
buttonPause=tk.Button(root,textvariable=pause_resume,command=buttonPauseClick)
buttonPause.place(x=140,y=10,width=50,height=20)

# 下一首
def buttonNextClick():
    global playing
    playing=False
    pygame.mixer.music.stop()
    pygame.mixer.quit()     # 退出
    buttonPlayClick()       # 重新播放一首
buttonNext=tk.Button(root,text='Next',command=buttonNextClick)
buttonNext.place(x=200,y=10,width=50,height=20)
buttonNext['state']='disabled'

musicName=tk.StringVar(root,value='None')
labelName=tk.Label(root,textvariable=musicName)     # 显示歌曲名称
labelName.place(x=0,y=40,width=270,height=20)

root.mainloop()