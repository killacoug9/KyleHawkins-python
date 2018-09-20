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



def boxstuff(boxWidth, boxLength):
    boxWidth = input("box width")
    boxLength = input('box length')
    print(int(boxLength) * int(boxWidth))
    return(boxWidth,boxLength)


#print('pee wee wee wee pee wee omg itz me time to bee a bee le mao yo bro eating fro yo ho oooooooooooooooo')





def doubleUp(list, z):
    result = [0]*4
    result[0] = list[0]*z
    result[1] = list[1]*z
    result[2] = list[2]*z
    result[3] = list[3]*z
    return(result)


results = doubleUp([1,2,3,4],2)
print(results)
results = doubleUp(results,3)
print(results)
results = doubleUp(results,4)
print(results)


