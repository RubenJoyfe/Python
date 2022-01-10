from turtle import *

def draw_1(sizes=3, widthSize=2, tam=10):
    width(widthSize)
    for i in range(sizes):
        forward(100/(sizes/tam))
        left(360/sizes)

def draw_star(x,y,length):
    penup()
    goto(x,y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)

def drawTistTost():
    width(20)
    bgcolor("black")
    colors=['#db0f3c', '#50ebe7', 'white']
    pos=[(0,0), (-5,13), (-5,5)]

    for (x,y), col in zip(pos, colors):
        up()
        goto(x,y)
        down()
        color(col)
        left(180)
        circle(50,270)
        forward(120)
        left(180)
        circle(50,90)

# draw_star(80,50,50)

# left(180)
# circle(50,270)




input("Press any key to continue")