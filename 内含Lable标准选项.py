#coding:utf-8
#内含Lable标准选项
import keyword
if 'print' in keyword.kwlist:
    from Tkinter import * 
else:
    from tkinter import *

root =Tk()
root.wm_title("辛星tkinter教程完全版")
w1=Label(root,text="跟着星哥一起学tkinter")
w1.pack()
root.mainloop()


'''
standard options：
activebackground，activeforeground，anchor（标记），background，bitmap（位图），
borderwidth（边境宽度），cursor(光标），disabledforeground，font，foreground，
highlightbackground，highlightcolor，highlightthickness，image，justify，
padx，pady，relief，takefocus，text，textvariable，underline，wraplength


widget-specific options：
height，state，width

翻译：


标准的选择：

activebackground，activeforeground，锚（标记），背景，位图（位图），

带（边境宽度），光标（光标），disabledforeground（禁用的背景）、字体、前景，

突出显示的背景，突出显示的颜色，突出显示的厚度（浓度），图像，证明，

padx，pady，减轻，takefocus（采取集中），文本，文本变量，下划线，
wraplength（包长度）



窗口小部件特定的选项：

高度，状态，宽度 

'''