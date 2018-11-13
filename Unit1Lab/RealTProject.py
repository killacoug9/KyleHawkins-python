import turtle as t
pen = t.Pen()

def main():
    line()
    square()
    circle()


def line():
    pen.up()
    pen.goto(-50,0)
    pen.down()
    pen.forward(100)

def square():
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
    pen.up()
    pen.goto(300,0)
    pen.down()
    pen.circle(300)





main()
t.exitonclick()
