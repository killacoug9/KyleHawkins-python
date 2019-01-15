import turtle as t
import random
pen = t.Pen()
t.bgcolor('white')
t.tracer(0,0)

# def clearT():
#     print('\n'*13)

input('press enter for rules')
print('In my game you will be able to chose different shapes, colors, sizes, etc. \n there are 3 different preset. advanced is the rossete,\n polygon you get to choose the size shape and color of a polygon,\n and foursquare is the foursquare project \n')




#shift F10 to run
#this is main
def main():
    BackGround()
    chooseGame()


####################################################################################################################################


#choose the background color
def BackGround():
    BackgroundColor = input('what color for background')
    t.bgcolor(BackgroundColor)


#this is how to chose color options

colorType = input('what color type..rgb, normal, random \n if its rgb you can choose the rgb values, if its normal u just type in a basic color, if its random then itll chose a random rgb color')##
useRGB = False

if colorType == 'rgb':
    useRGB = True
    t.colormode(255)
elif colorType == 'normal':
    colorUse = input('what color')

elif colorType == 'random':
    t.colormode(255)
    colorUse = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
else:
    print('i didnt understand your input, ill just use random color')
    t.colormode(255)
    colorUse = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

if useRGB == True:
    t.colormode(255)
    colorS1 = int(input('enter 1st rbg value'))
    colorS2 = int(input('second rbg value'))
    colorS3 = int(input('3rd rgb value'))
    colorUse = (colorS1, colorS2, colorS3)




pen.color(colorUse)




###################################
#this holds game choices
def chooseGame():
    whatGame = input('what images to see options are \n fourbox \n polygon \n advanced')

    if whatGame == 'fourbox':
        FourBoxShapes()

    elif whatGame == 'advanced':
        advanced()

    elif whatGame == 'polygon':
        makeOwnPoly()


##this id the roseette advanced thing

#######################################################################################################



def makeOwnPoly():
        sides = input('how many sides, within 3 and 20')
        length = input('how long, below 150')

        #these are the variables for the polygon
        # sides = 9
        # length = 70

        #pen.left(90)

        if abs(int(sides)) < 3:
            print('wow i know what youre doing') #counter for too little sides
            sides = random.randint(3, 20)



        if abs(int(length)) > 150:
            print('hey thats too long')
            length = random.randint(50, 150)

            # counter for too long

        if abs(int(sides)) > 20:
            print('no more than 20 sides') #counter for too many
            sides = random.randint(3, 20)


        angle = 360/abs((float(sides)))

        #this creates my polygon shape depending of how many sides and length were inputed
        pen.setheading(0)
        for x in range(0, abs(int(sides))):
            #colorUse

            #pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            pen.forward(abs(float(length)))
            pen.right(abs(float(angle)))



def advanced():
    t.colormode(255)
    print('this is a little beefy so it make take a second to load, be patient')
    SL = input('length between 5 and 30')
    #CL = input('length between 5 and 30')

    AdvChoice = input('do you want more inputs for the rosette. yes or no. i recomend no')
    if AdvChoice == 'yes':
        SL2 = input('length between about 100-300')
        #SL3 = input('length between about 100-500')

        CL2 = input('length between about 100-300')
        #CL3 = input('length between about 100-500')
    elif AdvChoice == 'no':
        print('good choice')
        SL2 = 300
        CL2 = 300


    def drawSquare(length):

        for i in range(4):
            pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))#change these to colorUse...
            pen.forward(length)
            pen.right(90)

    for i in range(60):
        pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        drawSquare(int(SL2))
        pen.right(9)

    # for i in range(750):
    #     pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    #     drawSquare(random.randint(100, 200))
    #     drawSquare(150)
    #     pen.right(25)

    def drawCircle(length):

        for i in range(4):
            pen.color(random.randint((0)+1,255), random.randint((0)+1,255), random.randint(0,255))
            pen.circle(length)
            pen.right(75)

    for i in range(60):
        #pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        drawCircle(int(CL2))
        pen.right(9)

    # for i in range(750):
    #     #pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    #     drawSquare(random.randint(100, 200))
    #     drawCircle(150)
    #     pen.right(25)

    drawSquare(length=int(SL))
    drawCircle(length=int(SL))



########################################################################################################################



#This is one of the pre set games for four square which is tri circle, square, and multi side in four corners of screen

def FourBoxShapes():
    t.colormode(255)

#     pen.clear()
    #t.setup(800,800)
#
#
# #centers it
    pen.up()
    pen.goto(0,0)
    pen.down()


#goes to the start point of FourSquare function
    pen.up()
    pen.goto(-250,300)
    pen.down()
    pen.left(35)
#
#
    def FPolygon():


        # sides = input('how many sides')
        # length = input('how long ')

        #these are the variables for the polygon
        sides = 9
        length = 70

        #pen.left(90)

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

    # this creates my polygon shape depending of how many sides and length were inputed
        pen.setheading(0)
        for x in range(0, abs(int(sides))):
            #colorUse

            pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            pen.forward(abs(float(length)))
            pen.right(abs(float(angle)))


###############

    #triangle top right

    def FTriangle():


        for x in range(0, 3):
            pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

        pen.up()
        pen.goto(150, 120)
        pen.down()

        #pen.right(90)
        pen.forward(200)
        pen.left(120)
        pen.forward(200)
        pen.left(120)
        pen.forward(200)









    ###############

    #circle, bottom left

    def FCircle():
        for x in range(0, 2):
            pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

        pen.up()
        pen.goto(-220, -250)
        pen.down()
        pen.setheading(0)
        pen.circle(100)

    ##################

    def FSquare():

        for x in range(0,4):
            pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

        pen.up()
        pen.goto(350, -275)
        pen.down()
        pen.setheading(180)

        pen.forward(200)
        pen.right(90)
        pen.forward(200)
        pen.right(90)
        pen.forward(200)
        pen.right(90)
        pen.forward(200)

 #now inside of foursquare i will call all individual shapes
    FPolygon()
    FTriangle()
    FCircle()
    FSquare()
















##############################



main()
t.update()
t.exitonclick()

