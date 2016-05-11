
#coding:utf-8
__metaclass__=type 
import keyword
if 'print' in keyword.kwlist:
    from Tkinter import * 
else:
    from tkinter import *

def xin():
	global root 
	#上面这行可以不要。
	Label(root,text='I love python').pack()

root =Tk()
menubar =Menu(root)

for x in ['vb','c','java','php']:
	menubar.add_command(label=x)

menubar.add_command(label='python',command=xin)

def pop(event):
	menubar.post(event.x_root,event.y_root)
	#上面的和下面的运行一样，所以root并不是又回到上面的代码root=Tk()。
	# menubar.post(event.x,event.y)
root.bind("<Button-3>",pop)
root.mainloop()













