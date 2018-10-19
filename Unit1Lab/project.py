def main():




    p1 = input('what is you decimal grade for period 1')
    p2 = input('what is you decimal grade for period 2')
    p3 = input('what is you decimal grade for period 3')
    p4 = input('what is you decimal grade for period 4')
    print("its starting")#starting
    listOfGPA = [p1, p2, p3, p4]
    num = len(listOfGPA)
    uncalculatedGPA = 0
    GPA = calculateGrades(listOfGPA, uncalculatedGPA)




########################################################################################split functions





def calculateGrades(listOfGPA, uncalculatedGPA):
    num = len(listOfGPA)
    for zz in listOfGPA:
        uncalculatedGPA = uncalculatedGPA + int(zz)
    input('puase')
    print('i just added them together')


    finishedMathGPA = uncalculatedGPA/num


    placeHolder = remarks(finishedMathGPA)
    remarks(finishedMathGPA)
    return finishedMathGPA

#######################################################################split functions





def remarks(x):
    if float(x) == 100:
        print("4.0 BABY")
    elif x >= 94.5:
        print("nice As bud")
    elif x >= 82.5:
        print('Bs okk')
    elif x >= 72.5:
        print('Cs whatever')
    elif x >= 62.5:
        print('Ds cmon')
    else:
        print('boo you suck failing classes stupid')

    return x


#################################################################################################calling main



main()
