from random import *


def main():
    loop = "y"
    timesRun = 0
    while loop == "y":
        timesRun = timesRun + 1
        y = findRandNum()
        print(createDie(y))
        print('lucky dog you got a ' + str(y))
        loop = input('do u wanna keep going y or n')











def findRandNum():
    x = randint(1,6)
    return x




def createDie(findRandNum):
    topandbottom = '-------'
    noneStar = '|      |'
    oneStarCenter = '|  *   |'
    oneStarRight = '|    * |'
    twoStar = '| *  * |'
    oneStarLeft = '| *    |'
    dice1 = [topandbottom, noneStar,oneStarCenter, noneStar, topandbottom]
    print(dice1)
main()
