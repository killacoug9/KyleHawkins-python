import turtle as t
import random
# #
t.tracer(0, 0)

pen = t.Pen()
t.colormode(255)





def drawSquare(length):
    for i in range(4):
        pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        pen.forward(length)
        pen.right(90)


for i in range(60):
    pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    drawSquare(300)
    pen.right(9)





for i in range(750):
    pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    #drawSquare(random.randint(100, 200))
    drawSquare(150)
    pen.right(25)



















C = 0
CC = 0
CCC = 0


def drawCircle(length):

    for i in range(4):
        pen.color(random.randint((0)+1,255), random.randint((0)+1,255), random.randint(0,255))
        pen.circle(length)
        pen.right(75)


for i in range(60):
    pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    drawCircle(300)
    pen.right(9)





for i in range(750):
    pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    #drawSquare(random.randint(100, 200))
    drawCircle(150)
    pen.right(25)





t.update()
t.exitonclick()

