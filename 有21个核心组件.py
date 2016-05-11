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
w2=Label(root,text='''

第三节:组件讲解以及按钮
*************tkinter 的核心组件************
1.在 Python 的 tkinter 中,有 21 个核心组件,它们提供
了最基本的功能,虽然简单,因为使用频率较高,因此特
别重要。

2.这 21 个核心组件是:Toplevel、Label、Button、
Canvas、Checkbutton、Entry、Frame、LabelFrame、
Listbox、Menu、Menubutton、Message、OptionMenu、
PaneWindow 、Radiobutton 、Scale 、Scrollbar 、Spinbox 、
Text、Bitmap、Image。

翻译：
顶层、标签、按钮、

帆布、多项选择的、进入、框架、label框架、

、菜单列表、菜单按钮、消息、菜单、

pane窗格、单选、规模、滚动条、纺纱箱、

文本，位图，图像
''')
w2.pack()
root.mainloop()