from random import *
DICENUM = 2


def main():
    loop = "y"
    timesRun = 0
    bigList = []
    setofdice = createdie

    while loop == "y":

        timesRun += 1

        Rnum1 = findRandNum()
        diceList = createDie(Rnum1)
        timesnum = input('how many die')

        for z in range(0, int(timesnum)):
            bigList.append(diceList[roll()])

        makeDice(bigList)
        bigList.clear()


        # print('lucky dog you got a ' + str(Rnum1))
        # print('youve run it ' + str(timesRun) + ' times')
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
    One = [topandbottom, noneStar, oneStarCenter, noneStar, topandbottom]
    two = [topandbottom,noneStar,twoStar,noneStar,topandbottom]
    three= [topandbottom,oneStarLeft,oneStarCenter,oneStarRight, topandbottom]
    four = [topandbottom, twoStar, noneStar, twoStar,topandbottom]
    five = [[topandbottom, twoStar, oneStarCenter, twoStar, topandbottom]]
    six = [topandbottom, twoStar, twoStar, twoStar,topandbottom]
    diceList = [One, two, three, four, five, six]




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
