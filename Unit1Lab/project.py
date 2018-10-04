def main():

    p1 = input('what is you decimal grade for period 1')
    p2 = input('what is you decimal grade for period 2')
    p3 = input('what is you decimal grade for period 3')
    p4 = input('what is you decimal grade for period 4')
    print("its starting")#starting
    listOfGPA = [p1, p2, p3, p4]
    num = len(listOfGPA)
    GPA = calculateGrades(listOfGPA, num)
    print(GPA)
 #   return GPA
 #   return num
    placeHolder = remarks(GPA)


def calculateGrades(listOfGPA,num):
    uncalculatedGPA = 0
    for zz in listOfGPA:
        uncalculatedGPA = int(zz) + int(uncalculatedGPA)




#    if len(listOfGPA) == 4:
#        uncalculatedGPA = float(listOfGPA[0]) + float(listOfGPA[1]) + float(listOfGPA[2]) + float(listOfGPA[3])
#    elif len(listOfGPA) == 5:
#        uncalculatedGPA = float(listOfGPA[0]) + float(listOfGPA[1]) + float(listOfGPA[2]) + float(listOfGPA[3]) + float(listOfGPA[4])
#    elif len(listOfGPA) == 6:
#        uncalculatedGPA = float(listOfGPA[0]) + float(listOfGPA[1]) + float(listOfGPA[2]) + float(listOfGPA[3]) + float(listOfGPA[4]) + float(listOfGPA[5])



    finishedMathGPA = uncalculatedGPA / num
     #   print(finishedMathGPA)##this is printing YOUR GPA THIS IS WHAT I WANT

    return finishedMathGPA


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




main()
