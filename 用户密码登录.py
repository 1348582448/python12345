#coding:utf-8

import keyword
if 'print' in keyword.kwlist:
    from Tkinter import * 
else:
    from tkinter import *


def reg():
	s1=e1.get()
	s2=e2.get()
	t1=len(s1)
	t2=len(s2)
	if s1=="111" and s2 =="222":
		c["text"]="登陆成功"
	else:
		c["text"]="用户名或密码错误"
		e1.delete(0,t1)
		#删除0-t1位置的文本，对比range（0，t1）理解。
		e2.delete(0,t2)

root =Tk()
l=Label(root,text ="用户名：")
l.grid(row=0,column=0,sticky=W)

e1=Entry(root)
e1.grid(row=0,column=1,sticky=E)

l2=Label(root,text="密码:")
l2.grid(row=1,column=0,sticky=W)

e2=Entry(root)
e2['show']='*'
e2.grid(row=1,column=1,sticky=E)

b=Button(root,text="登陆",command=reg)
b.grid(row=2,column=1,sticky=E)

c=Label(root,text="")
c.grid(row=3)
root.mainloop()



