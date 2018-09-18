#from random import *

#def aboutME():
#    print('i go to bellarmine')
#    print('i like python')
#aboutME()

#def number2():
 #   years = input ("what grade ar you in, in numbers")
#    print ('you have been going to school for ' + (str(years)) + " years")

#number2()

from random import *

#def num3():
#    print('what city do you live in')
#    city = input()
#    print('you live in ' + city)
#
#num3()


def twonumbers():
    x = input("start number")
    y = input("end input")
    myNumber = randint(int(x), int(y))
    print(str(myNumber)+ ' is a random numb btween')
    print (str(x) + ' and ' + str(y))


twonumbers()

def boxstuff():
    boxWidth = input("box width")
    boxLength = input('box length')
    print(int(boxLength) * int(boxWidth))

boxstuff()


