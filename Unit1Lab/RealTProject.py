import turtle as t
import random
pen = t.Pen()
t.bgcolor('grey')

def main():
    line()
    square()
    circle()
    triangle()
    pen.clear()
    adv()
    space()

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

    # colorType = input('what color type rgb or normal, random')
    # useRGB = False
    #
    # if colorType == 'rgb':
    #     useRGB = True
    # else:
    #     useRGB = False
    #
    #
    # if colorType == 'normal':
    #     colorChoice = input('what color')
    #
    # if useRGB == True:
    #     colorS1 = input('enter 1st rbg value')
    #     colorS2 = input('second rbg value')
    #     colorS3 = input('3rd rgb value')
    #     colorUse = pen.color(colorS1, colorS2, colorS3)
    # else:
    #     colorUse = pen.color(colorChoice)
    #
    # if colorType == 'random':
    #     colorUse = pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    #
    # sides = input('how many sides')
    # length = input('how long ')
    pen.left(90)

    sides = 12
    length=100



    if abs(int(sides)) < 3:
        print('wow i know what youre doing') #counter for too little sides
        sides = random.randint(3, 20)

    if abs(int(length)) > 200:
        print('hey thats too long')
        length = random.randint(50, 200) # counter for too long

    if abs(int(sides)) > 20:
        print('no more than 20 sides') #counter for too many
        sides = random.randint(3, 20)


    angle = 360/abs((float(sides)))

    for x in range(0, abs(int(sides))):
        #colorUse

        pen.color(random.randint(0,255), random.randint(0+20,255), random.randint(0,255))
        pen.forward(abs(float(length)))
        pen.right(abs(float(angle)))

def space():
    pen.clear()
    t.setup(800,800)
    pen.up()
    pen.goto(0,0)
    pen.down()

    pen.up()
    pen.goto(-200,200)
    pen.down()
    pen.left(35)

    #
    # sides = input('how many sides')
    # length = input('how long ')
    sides=9
    length=70
    pen.left(90)


    if abs(int(sides)) < 3:
        print('wow i know what youre doing') #counter for too little sides
        sides = random.randint(3, 20)

    if abs(int(length)) > 100:
        print('hey thats too long')
        length = random.randint(50, 100) # counter for too long

    if abs(int(sides)) > 20:
        print('no more than 20 sides') #counter for too many
        sides = random.randint(3, 20)


    angle = 360/abs((float(sides)))

    for x in range(0, abs(int(sides))):
        #colorUse

        pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        pen.forward(abs(float(length)))
        pen.right(abs(float(angle)))
####################################################################################
#triangle top right
    for x in range(0, 3):
        pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    pen.up()
    pen.goto(200, 200)
    pen.down()
    pen.right(90)
    pen.forward(200)
    pen.left(120)
    pen.forward(200)
    pen.left(120)
    pen.forward(200)









###############
#circle, bottom left
    for x in range(0, 2):
        pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

    pen.up()
    pen.goto(-300, -220)
    pen.down()
    pen.circle(100)
########################################
#square
    for x in range(0,4):
        pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    pen.up()
    pen.goto(270, -275)
    pen.down()

    pen.right(65)
    pen.forward(200)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(200)








##############################



main()
t.exitonclick()
t.update()
