# tutle()函数用法
# 1.turtle绘图窗体
# turtle。setup(width,height,startx,starty)
# turtle的空间/角度坐标体系
#                     y
#                     |90/-270度
#  (-100,100)         |            (100,100)
# 180/-180度          |                   0/360度
# ---------------------------------------------x
# (-100,-100)        | (0,0)       (100,-100)
#                    |
#                    |270/-90度
# turtle的移动
# turtle.goto(x,y)
# import turtle
# turtle.setup(1000,1000)
# turtle.goto(-100,100)
# turtle.circle(r,angle)画圆
# turtle.circle(r,extent=NONE)据半径绘制extent角度的弧形
# turtle.bk(d)当前距离后退
# turtle.fd(d)当前距离前进
# turtle.seth(angle)改变前进方向
# turtle.right(angle)向右转
# turtle.left(angle)向左转
# RGB色彩模式
# turtle.colormode(mode)
# turtle.penup()抬起画笔turtle.pu()
# turtle.pendown()落下画笔turtle.pd()
# turtle.pensize()画笔宽度turtle.width(width)
# turtle.pencolor(color)画笔颜色color可以是颜色字符串或rgb值
# ###################Jieba()函数用法
# import jieba
# s = '我们明天要做核酸检测，但是我却要请假'
# r = jieba.cut(s, cut_all=True)
# m = jieba.cut(s, cut_all=False)
# print('/'.join(r))
# print('/'.join(m))
import turtle

# I
#  turtle.pu()
#  turtle.pensize(10)
#  turtle.pencolor(0, 0, 1)
#  turtle.goto(-180, 180)
#  turtle.pd()
#  turtle.fd(100)
#  turtle.bk(50)
#  turtle.right(100)
#  turtle.fd(150)
#  turtle.left(100)
#  turtle.fd(50)
#  turtle.bk(100)
#  turtle.fd(100)
#  turtle.done()
# ❤️
import turtle
turtle.pu()
turtle.goto(180, 90)
turtle.pensize(5)
turtle.pencolor('red')
turtle.speed(10)
turtle.pd()
turtle.begin_fill()
turtle.left(90)
turtle.circle(100, 180)
turtle.right(180)
turtle.circle(100, 180)
turtle.circle(200, 180)
turtle.color('red')
turtle.end_fill()
turtle.done()
