#    if len(listOfGPA) == 4:
#        uncalculatedGPA = float(listOfGPA[0]) + float(listOfGPA[1]) + float(listOfGPA[2]) + float(listOfGPA[3])
#    elif len(listOfGPA) == 5:
#        uncalculatedGPA = float(listOfGPA[0]) + float(listOfGPA[1]) + float(listOfGPA[2]) + float(listOfGPA[3]) + float(listOfGPA[4])
#    elif len(listOfGPA) == 6:
#        uncalculatedGPA = float(listOfGPA[0]) + float(listOfGPA[1]) + float(listOfGPA[2]) + float(listOfGPA[3]) + float(listOfGPA[4]) + float(listOfGPA[5])

    #finishedMathGPA = uncalculatedGPA / num
     #   print(finishedMathGPA)##this is printing YOUR GPA THIS IS WHAT I WANT

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
