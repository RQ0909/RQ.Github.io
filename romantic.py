from turtle import *
import tkinter as tk
from tkinter import Button

def draw_rose():
    #设置绘制起点
    setup (700,700)
    #画笔颜色
    pencolor("red")
    hideturtle()
    penup()
    goto(0,280)
    pendown()
    left(135)
    speed(120)
#左侧弧形绘制
a=0.2
for i in range (80):
    if i < 50:
        pensize(a)
        forward(2)
        a+=0.15
        if i<10:
            left(0.7)
        elif 10<i<24:
            left(1)
        elif 24<i<40:
            left(3)
        elif 40<i<50:
            left(4)
    elif i >=50:
        pensize(a)
        forward(2.2)
        a-=0.25
        if 50<i<65:
            left(6.7)
        elif 65<i<80:
            left(2)
setheading(0)
penup()
goto(40,305)
pendown()
left(145)
#右侧弧形绘制
a=0.1
for i in range (100):
    if i < 60:
        pensize(a)
        forward(3)
        a+=0.15
        if i<10:
            left(0.8)
        elif 10<i<24:
            left(0.8)
        elif 24<i<40:
            left(1.7)
        elif 40<i<60:
            left(2.2)
    elif i >=60:
        pensize(a)
        forward(2.4)
        a-=0.15
        if 60<i<85:
            left(3.2)
        elif 85<i<90:
            left(4)
setheading(0)
penup()
goto(45,320)
pendown()
left(10)
a=0.1
for i in range (100):
    if i < 60:
        pensize(a)
        forward(3)
        a+=0.15
        if i<17:
            right(3.2)
        elif 17<i<20:
            right(3.5)
        elif 20<i<40:
            right(6.8)
        elif 40<i<50:
            right(0.6)
        elif 50<i<60:
            left(1)
    elif i >=60:
        pensize(a)
        forward(2.4)
        a-=0.16
        if 60<i<85:
            left(0.4)
        elif 85<i<90:
            left(1)
setheading(0)
penup()
goto(-135,265)
pendown()
left(160)
a=0.1
for i in range (120):
    if i < 60:
        pensize(a)
        forward(3)
        a+=0.15
        if i<10:
            left(2)
        elif 10<i<15:
            left(8)
        elif 15<i<35:
            left(6)
        elif 35<i<40:
            left(4)
        elif 40<i<60:
            left(1)
    elif i >=60:
        pensize(a)
        forward(3)
        a-=0.15
        if 60<i<90:
            right(0.4)
        elif 90<i<120:
            right(0.8)
setheading(0)
penup()
goto(80,250)
pendown()
left(245)
a=0.2
for i in range (80):
    if i < 40:
        pensize(a)
        forward(1.2)
        a+=0.15
        if i<15:
            left(0.6)
        elif 15<i<40:
            left(0.3)
    elif i >=40:
        pensize(a)
        forward(1.2)
        a-=0.15
        if 40<i<65:
            left(0.6)
        elif 65<i<80:
            left(0.35)
setheading(0)
penup()
goto(-150,195)
pendown()
left(300)
a=0.2
for i in range (80):
    if i < 40:
        pensize(a)
        forward(1.2)
        a+=0.16
        if i<15:
            right(0.6)
        elif 15<i<40:
            right(0.3)
    elif i >=40:
        pensize(a)
        forward(1.2)
        a-=0.16
        if 40<i<65:
            right(0.6)
        elif 65<i<80:
            right(0.35)
setheading(0)
penup()
goto(-205,225)
pendown()
left(194)
a=0.1
for i in range (100):
    if i < 50:
        pensize(a)
        forward(3)
        a+=0.15
        if i<10:
            left(7)
        elif 10<i<30:
            left(3)
        elif 30<i<50:
            left(0.1)
    elif i >=50:
        pensize(a)
        forward(3)
        a-=0.15
        if 50<i<80:
            right(0.3)
        elif 80<i<100:
            right(0.6)
setheading(0)
penup()
goto(110,280)
pendown()
left(6)
a=0.1
for i in range (120):
    if i < 60:
        pensize(a)
        forward(3)
        a+=0.15
        if i<10:
            right(4.5)
        elif 10<i<30:
            right(5)
        elif 30<i<60:
            right(0.1)
    elif i >=60:
        pensize(a)
        forward(3)
        a-=0.15
        if 50<i<80:
            left(0.6)
        elif 80<i<100:
            left(0.9)
setheading(0)
penup()
goto(-160,110)
pendown()
left(283)
a=0.2
for i in range (80):
    if i < 40:
        pensize(a)
        forward(2.4)
        a+=0.15
        if i<10:
            right(0.6)
        elif 15<i<40:
            right(0.1)
    elif i >=40:
        pensize(a)
        forward(2.4)
        a-=0.15
        if 40<i<65:
            left(2)
        elif 65<i<80:
            left(3)
setheading(0)
penup()
goto(90,155)
pendown()
left(258)
a=0.2
for i in range (80):
    if i < 40:
        pensize(a)
        forward(3)
        a+=0.15
        if i<10:
            left(0.8)
        elif 15<i<40:
            left(0.1)
    elif i >=40:
        pensize(a)
        forward(3)
        a-=0.15
        if 40<i<65:
            right(2)
        elif 65<i<80:
            right(3)
setheading(0)
penup()
goto(-60,-45)
pendown()
right(9)
a=0.2
for i in range (40):
    if i < 20:
        pensize(a)
        forward(1.3)
        a+=0.15
        if i<5:
            left(0.7)
        elif 5<i<20:
            left(0.4)
    elif i >=20:
        pensize(a)
        forward(1.3)
        a-=0.15
        if 20<i<35:
            left(0.7)
        elif 35<i<40:
            left(0.4)
setheading(0)
penup()
goto(-70,-55)
pencolor("green")
pendown()
right(170)
a=0.2
for i in range (80):
    if i <40 :
        pensize(a)
        forward(2)
        a+=0.15
        if i<25:
            right(0.5)
        elif 25<i<40:
            right(1)
    elif i >=40:
        pensize(a)
        forward(2.5)
        a-=0.15
        if 40<i<55:
            right(1)
        elif 55<i<70:
            right(2)
        elif 70<i<80:
            right(1)
setheading(270)
left(30)
a=0.2
for i in range (80):
    if i <40 :
        pensize(a)
        forward(2.5)
        a+=0.15
        if i<25:
            left(0.5)
        elif 25<i<40:
            left(1)
    elif i >=40:
        pensize(a)
        forward(3)
        a-=0.15
        if 40<i<55:
            left(2)
        elif 55<i<70:
            left(1.3)
        elif 70<i<80:
            left(1)
setheading(270)
penup()
goto(20,-55)
pendown()
left(65)
a=0.2
for i in range (60):
    if i <30 :
        pensize(a)
        forward(2)
        a+=0.15
        if i<15:
            left(1)
        elif 15<i<30:
            left(2)
    elif i >=30:
        pensize(a)
        forward(2.5)
        a-=0.15
        if 30<i<45:
            left(2)
        elif 45<i<50:
            left(2.5)
        elif 50<i<60:
            left(1.5)
setheading(270)
right(17)
a=0.2
for i in range (80):
    if i <40 :
        pensize(a)
        forward(2.2)
        a+=0.15
        if i<25:
            right(1)
        elif 25<i<40:
            right(2)
    elif i >=40:
        pensize(a)
        forward(2.5)
        a-=0.15
        if 40<i<55:
            right(2)
        elif 55<i<70:
            right(1.5)
        elif 70<i<80:
            right(0.6)
setheading(0)
penup()
pencolor("brown")
goto(-49,-90)
pendown()
right(89)
a=1
for i in range (120):
    if i < 60:
        pensize(a)
        forward(3.5)
        a+=0.08
    elif i >=60:
        pensize(a)
        forward(3.5)
        a-=0.08
setheading(0)
penup()
goto(-16,-70)
pendown()
right(91)
a=1
for i in range (120):
    if i < 60:
        pensize(a)
        forward(3.5)
        a+=0.08
    elif i >=60:
        pensize(a)
        forward(3.5)
        a-=0.08
setheading(0)

speed(1)
penup()
goto(-16,-150)
pendown()
pensize(3)
left(35)
forward(15)
setheading(0)
right(115)
forward(34)

setheading(180)
penup()
goto(-49,-250)
pendown()
pensize(3)
right(35)
forward(15)
setheading(180)
left(115)
forward(34)
input()
done

# 创建主窗口
root = tk.Tk()
root.title("玫瑰花绘制")
root.geometry("600x150")
root.configure(bg='pink')

# 添加开始按钮
start_button = Button(root, text="开始绘制", command=draw_rose)
start_button.pack(pady=20)

root.mainloop()
