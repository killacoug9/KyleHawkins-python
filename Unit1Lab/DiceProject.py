from random import *


def main():
    loop = "y"
    timesRun = 0

    while loop == "y":

        timesRun = timesRun + 1
        y = findRandNum()
        print(createDie(y))
        print('lucky dog you got a ' + str(y))
        print('youve run it ' + str(timesRun) + ' times')
        loop = input('do u wanna keep going y or n')






def findRandNum():
    x = randint(1,6)
    return x






def createDie(findRandNum):
    topandbottom = '--------'
    noneStar = '|      |'
    oneStarCenter = '|  *   |'
    oneStarRight = '|    * |'
    twoStar = '| *  * |'
    oneStarLeft = '| *    |'
    diceNumber1 = ['']
    if findRandNum == 1:
        diceNumber1 = [topandbottom, noneStar, oneStarCenter, noneStar, topandbottom]
    elif findRandNum == 2:
        diceNumber1 = [topandbottom,noneStar,twoStar,noneStar,topandbottom]
    elif findRandNum == 3:
        diceNumber1 = [topandbottom,oneStarLeft,oneStarCenter,oneStarRight, topandbottom]
    elif findRandNum == 4:
        diceNumber1 = [topandbottom, twoStar, noneStar, twoStar,topandbottom]
    elif findRandNum == 5:
        diceNumber1 = [topandbottom, twoStar, oneStarCenter, twoStar, topandbottom]
    elif findRandNum == 6:
        diceNumber1 = [ topandbottom, twoStar, twoStar, twoStar,topandbottom]

    firstplace = diceNumber1

    for LinesToPrint in firstplace:
        print(LinesToPrint)



    # one = [topandbottom, noneStar, oneStarCenter, noneStar, topandbottom]
    # two = [topandbottom,noneStar,twoStar,noneStar,topandbottom]
    # three = [topandbottom,oneStarLeft,oneStarCenter,oneStarRight, topandbottom]
    # four = [topandbottom, twoStar, noneStar, twoStar,topandbottom]
    # five = [topandbottom, twoStar, oneStarCenter, twoStar, topandbottom]
    # six = [ topandbottom, twoStar, twoStar, twoStar,topandbottom]








main()
