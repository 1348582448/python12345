#coding:utf-8

import keyword
if 'print' in keyword.kwlist:
    from Tkinter import * 
else:
    from tkinter import *

root=Tk()

menubar=Menu(root) 
fmenu=Menu(menubar)
'''
上面这两行，其实可以这么理解
Menu是一个构造方法，就是通过传入一个参数建立一个
菜单，第二行又相当于嵌套，把这个新建的菜单作为
参数又建立下一级菜单。

'''
for item in ['新建','打开','保存','另存为']:
	fmenu.add_command(label=item)

emenu=Menu(menubar)
for item in ['复制','粘贴','剪切']:
	emenu.add_command(label=item)

vmenu=Menu(menubar)
for item in ['默认视图','新式视图']:
	vmenu.add_command(label=item)

amenu=Menu(menubar)
for item in ['版权信息','其他说明']:
	amenu.add_command(label=item)


menubar.add_cascade(label='文件',menu=fmenu)
menubar.add_cascade(label='编辑',menu=emenu)
menubar.add_cascade(label='视图',menu=vmenu)
menubar.add_cascade(label='关于',menu=amenu)
# menubar.add_cascade(label='关于')
# menubar.add_cascade(menu=vmenu)
'''
从上面两行可以看出，可以分开写。
'''


# root.add_cascade(menu=menubar)
# root.add_command(menu=menubar)
# Tk().add_cascade(menu=menubar)
# Tk().add_command(menu=menubar)
# root(menu=menubar)
'''
上面这几行中的menu=fmenu，就是与代码开头的相反过程，
就是又把子菜单fmenu，emenu等又通过属性menu
（因为label与menu颜色同，所以是同label一样是属性）
类似字典一样绑定回上一级菜单。所以menu=fmenu相当于
menubar['menu'=fmenu]。但可能不能这么写，这个
键值对绑定的过程要在add_cascade中进行。
root['menu']=menubar是绑定回最上一级菜单，
相当于root["menu"=menubar]。

下面注释的几行，是用来测试的，但都不成功，不能通过
这样的键值对赋值绑定。
注意修改为这样root(menu=menubar)，虽然颜色与之前的
相同了，但报错提示：
AttributeError: Tk instance has no __call__ method
'''

# menubar.add_cascade(label='关于')
# menubar(menu=vmenu)
'''
上面两行报错：
AttributeError: Menu instance has no __call__ method
'''

# menubar.add_cascade(label='关于')
# menubar.append(menu=vmenu)
'''
上面两行报错：
AttributeError: Menu instance has no attribute 'append'
'''

root['menu']=menubar
root.mainloop()



