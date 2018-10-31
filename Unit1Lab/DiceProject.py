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


    diceList = createDie(findRandNum)
    makeDice(diceList)




def makeDice(diceList):
    #print(diceList)

    for i in range(0, len(diceList[0])):

        for sublist in diceList:
            print(sublist[0])






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
    dice1 = ''
    dice2 =''
    dice3 =''
    dice4=''
    dice5=''
    dice6=''
    if findRandNum == 1:
        dice1 = [topandbottom, noneStar, oneStarCenter, noneStar, topandbottom]
    elif findRandNum == 2:
        dice2 = [topandbottom,noneStar,twoStar,noneStar,topandbottom]
    elif findRandNum == 3:
        dice3 = [topandbottom,oneStarLeft,oneStarCenter,oneStarRight, topandbottom]
    elif findRandNum == 4:
        dice4 = [topandbottom, twoStar, noneStar, twoStar,topandbottom]
    elif findRandNum == 5:
        dice5 = [topandbottom, twoStar, oneStarCenter, twoStar, topandbottom]
    elif findRandNum == 6:
        dice6 = [ topandbottom, twoStar, twoStar, twoStar,topandbottom]


    dice1 = [topandbottom, noneStar, oneStarCenter, noneStar, topandbottom]
    dice2 = [topandbottom,noneStar,twoStar,noneStar,topandbottom]
    dice3 = [topandbottom,oneStarLeft,oneStarCenter,oneStarRight, topandbottom]
    dice4 = [topandbottom, twoStar, noneStar, twoStar,topandbottom]
    dice5 = [topandbottom, twoStar, oneStarCenter, twoStar, topandbottom]
    dice6 = [ topandbottom, twoStar, twoStar, twoStar,topandbottom]


    diceList = [dice1, dice2, dice3, dice4, dice5,dice6]

    return diceList










main()
