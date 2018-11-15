import turtle as t
pen = t.Pen()
t.bgcolor('grey')

def main():
    line()
    square()
    circle()
    triangle()
    pen.clear()
    adv()

def line():
    t.colormode(255)
    pen.color(50,205,50)
    pen.up()
    pen.goto(-50,0)
    pen.down()
    pen.forward(100)

def square():
    t.colormode(hex)
    pen.color('#0000ff')
    pen.up()
    pen.goto(-100,100)
    pen.down()
    pen.forward(200)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(200)

def circle():

    pen.color('red')
    pen.up()
    pen.goto(300,0)
    pen.down()
    pen.circle(300)

def triangle():
    pen.color
    pen.up()
    pen.goto(-200, -150)
    pen.down()
    pen.right(90)
    pen.forward(400)
    pen.left(120)
    pen.forward(400)
    pen.left(120)
    pen.forward(400)


def adv():
    pen.up()
    pen.goto(0,0)
    pen.down()

    sides = input('how many sides')
    length = input('how long ')
    pen.left(90)

    angle = 180*(float(sides)-2)/float(sides)

    for x in range(0, int(sides)):
        pen.forward(float(length))
        pen.right(float(angle))







main()
t.exitonclick()
t.update()
