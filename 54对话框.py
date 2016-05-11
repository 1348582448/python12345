#coding:utf-8
#tkinter中关于对话框和消息框的代码。
__metaclass__=type 
import keyword
if 'print' in keyword.kwlist:
    from Tkinter import * 
else:
    from tkinter import *

from Dialog import *


'''
书上原本代码如下：
from Tkinter.dialog import *
from Tkinter import *
但实际运行提示No module named dialog。后来修改成上面代码那样”
from Dialog import * “运行成功。小刘老师说是版本，这应该是
python3.0以上版本。

'''
def xin():
	d=Dialog(None,title="2014辛星",text="2014年度辛星\
tkinter材料还满意吗？",bitmap=DIALOG_ICON,default=0,\
strings=("不满意","还可以","很满意"))
	print (d.num)

t=Button(None,text="辛星调查",command=xin)
t.pack()
b=Button(None,text="关闭",command=t.quit)
b.pack()
t.mainloop()














