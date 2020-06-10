import os
os.chdir('C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38')
import easygui as g
import random
y = random.randint(1,1000)
x = g.enterbox(msg='请输入要猜的数字', title='猜数字小游戏', default='', strip=True, image=None, root=None)
def gussy(x):
    if x == y:
        g.msgbox('恭喜你猜对了')
    elif x < y:
        x = g.enterbox(msg='小了！请重新输入要猜的数字', title='猜数字小游戏', default='', strip=True, image=None, root=None)
        gussy(x)
    elif x > y:
        x = g.enterbox(msg='大了！请重新输入要猜的数字', title='猜数字小游戏', default='', strip=True, image=None, root=None)
        gussy(x)
        
        
        

       可删除
