import turtle as turtle
pen = turtle.Pen()





 # imports the module turtle,
                    #* stands for all, which makes things easier

 # sets the speed of drawing to 0, which is the fastest
pen.color('white') # sets the color of the pen/lines to white
turtle.bgcolor('black') # sets the color of the background/canvas to black

x = 0 # creates a variable x with value 0




pen.up()


#note fd() means move forward, bk() means move back
# rt() or lt() means tilt right by a certain angle


pen.down() # sets down the pen, so that turtle can draw
# while the value of x is lesser than 120,

            #continuously do this:


# pen.forward(200)
# pen.right(90)
# pen.forward(200)
# pen.up()
# pen.goto(0,0)### i need to chill
# pen.down()
# pen.forward(200)
# pen.right(90)
# pen.forward(200)
#
#pene


pen.begin_fill()
turtle.colormode(255)
pen.fillcolor(245,255,250)
pen.pencolor(234, 45, 89)
pen.left(90)
pen.forward(200)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(200)
pen.end_fill()


#creates pene
pen.begin_fill()
pen.fillcolor('green')
pen.pencolor('purple')
#rightnut
pen.left(90)
pen.forward(70)
pen.right(90)
pen.forward(70)
pen.right(90)
pen.forward(70)
pen.right(90)
pen.forward(70)
#right nut
pen.end_fill()
#leftnut

pen.pencolor('red')
pen.begin_fill()
pen.fillcolor('blue')



pen.goto(0,0)
pen.left(90)
pen.forward(70)
pen.left(90)
pen.forward(70)
pen.left(90)
pen.forward(70)
pen.left(90)
pen.forward(70)

pen.end_fill()

#leftnut

pen.pencolor('purple')


pen.pencolor('black')
#shaftdetail/
pen.up()
pen.goto(0,160)
pen.down()
pen.right(90)
pen.forward(50)
pen.left(180)
pen.forward(25)
pen.right(90)
pen.up()
pen.forward(20)
pen.down()
pen.forward(20)





# rt(61)
#  fd(200)
# rt(61)
# fd(200)
# rt(61)
# fd(200)
# rt(61)
# fd(200)
# rt(61)
#  fd(200)
# rt(61)

turtle.exitonclick()

# When you click, turtle exits.

#That's all! Try customizing the script! 8)

