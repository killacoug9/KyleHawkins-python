from random import *


def main():
    loop = "y"
    timesRun = 0
    bigList = []


    while loop == "y":

        timesRun = timesRun + 1

        Rnum1 = findRandNum()
        diceList = createDie(Rnum1)
        timesnum = input('how many die')

        for z in range(0, int(timesnum)):
            bigList.append(diceList[roll()])

        makeDice(bigList)



        print('lucky dog you got a ' + str(Rnum1))
        print('youve run it ' + str(timesRun) + ' times')
        loop = input('do u wanna keep going y or n')

















def findRandNum():
    Rnum1 = randint(1,6)

    return Rnum1







def createDie(findRandNum):

    topandbottom = '--------'
    noneStar = '|      |'
    oneStarCenter = '|  *   |'
    oneStarRight = '|    * |'
    twoStar = '| *  * |'
    oneStarLeft = '| *    |'
    diceList = []

    diceList.append([topandbottom, noneStar, oneStarCenter, noneStar, topandbottom])

    diceList.append([topandbottom,noneStar,twoStar,noneStar,topandbottom])

    diceList.append([topandbottom,oneStarLeft,oneStarCenter,oneStarRight, topandbottom])

    diceList.append([topandbottom, twoStar, noneStar, twoStar,topandbottom])

    diceList.append([topandbottom, twoStar, oneStarCenter, twoStar, topandbottom])

    diceList.append([ topandbottom, twoStar, twoStar, twoStar,topandbottom])




    return diceList

def makeDice(diceList):
    #print(diceList)

    for row in range(0, len(diceList[0])):
        for col in range(0,len(diceList)):
            print (diceList[col][row], end='\t')
        print()




def roll():
    randomnum1 = randint(0,6)

    return randomnum1


main()
