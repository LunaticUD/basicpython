# Turtle库
import random
import turtle


# TODO:绘图窗体大小TODO:——>turtle.setup(width,height,startx,starty)TODO:
# TODO:turtle移动——>turtle.goto(x,y)TODO:
# 画圆的用法——>TODO:turtle.circle(r,angle)TODO:
# 当前距离后退——>turtle.bk(d)TODO:
# 当前距离前进——>turtle.fd(d)TODO:
# turtle.seth(angle)——>绝对度数TODO:
# seth()改变海龟行进方向；
# angle为据对度数；
# seth()只改变呢方向但是不行进；
# turtle.right(angle)
# turtle.left(angle)
# turtle.colormode(mode)
# turtle.penup():表示抬起画笔，海龟在飞行；可以简写成turtle.pu()TODO:
# turtle.pendown():表示画笔落下，海龟在爬行；可以简写成turtle.pd()TODO:
# turttle.pensize(width):表示画笔的宽度，也可以使用turtle.width(width)
# turtle.pencolor(color):color为颜色字符串或者 RGB值；
# turtle.forward(d):向前行进距离；可以简写为turtle.fd(d)，d为整数可以为负数；
# turtle.circle(r,extent=NONE):根据半径r绘制extent角度的弧形，
# r默认在圆心左侧R距离的位置；extent:绘制角度默认360度是整圆；
# turtle.pencolor('blue')
# turtle.width(5)
# turtle.circle(100)
# turtle.done()
# 五彩斑斓的心
def xin(a, b):
    turtle.setup(1000, 1000, 0, 0)
    turtle.seth(90)
    #TODO:
    turtle.penup()
    turtle.setx(random.randint(1, 150))
    turtle.sety(random.randint(1, 150))
    turtle.pendown()
    #TODO:
    turtle.pencolor(b)
    #TODO:
    turtle.fillcolor(b)
    #TODO:
    turtle.begin_fill()
    turtle.circle(a, 180)
    turtle.circle(2 * a, 90)
    turtle.circle(2 * a, 90)
    turtle.circle(a, 180)
    turtle.end_fill()
    #TODO:
    pass


y = ['red', 'blue', 'white', 'yellow', 'magenta', 'cyan', 'black', 'seashell', 'gold', 'pink', 'brown', 'purple']
for i in range(11):
    x = [random.randint(1, 50)]
    # r = random.sample(y, 1)
    xin(x[0], y[i])
    pass
turtle.done()
