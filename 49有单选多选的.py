#coding:utf-8
#有单选多选的，有下划分隔线
__metaclass__=type 
import keyword
if 'print' in keyword.kwlist:
    from Tkinter import * 
else:
    from tkinter import *

root=Tk()
m=Menu(root)
class ceshi:
	m2=Menu(m)
	for item in ['python','perl','php','ruby']:
		m2.add_checkbutton(label=item)

	m2.add_separator()

	for item in ['java','c++','c']:
		m2.add_radiobutton(label=item)

	m.add_cascade(label="lan",menu=m2)
	root['menu']=m
ceshi()
root.mainloop()














