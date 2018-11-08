from random import *


def main():

    loop = "y"
    timesRun = 0
    diceList = [0]*6
    diceList = createDie()


    while loop == "y":
        DICENUM = int(input('how many nums'))
        bigList = [0]*DICENUM
        timesRun += 1




        for z in range(0, DICENUM):
            rolling = findRandNum()

            bigList[z] = (diceList[rolling])





        makeDice(bigList)
        loop = input('do u wanna keep going y or n')



def findRandNum():
    Rnum1 = randint(0,5)

    return Rnum1







def createDie():

    topandbottom = '--------'
    noneStar = '|      |'
    oneStarCenter = '|  *   |'
    oneStarRight = '|    * |'
    twoStar = '| *  * |'
    oneStarLeft = '| *    |'
    diceList = [0]*6
    for num in range(0,6):
        if num == 0:
            diceList[num] = [topandbottom, noneStar, oneStarCenter, noneStar, topandbottom]
        elif num == 1:
            diceList[num] = [topandbottom,noneStar,twoStar,noneStar,topandbottom]
        elif num == 2:
            diceList[num] = [topandbottom,oneStarLeft,oneStarCenter,oneStarRight, topandbottom]
        elif num == 3:
            diceList[num] = [topandbottom, twoStar, noneStar, twoStar,topandbottom]
        elif num == 4:
            diceList[num] = [topandbottom, twoStar, oneStarCenter, twoStar, topandbottom]
        elif num == 5:
            diceList[num] = [ topandbottom, twoStar, twoStar, twoStar,topandbottom]





    return diceList

def makeDice(diceList):


    for row in range(0, len(diceList[0])):
        for col in range(0,len(diceList)):
            print (diceList[col][row], end='\t')
        print()




def roll():
    randomnum1 = randint(0,6)

    return randomnum1


main()
