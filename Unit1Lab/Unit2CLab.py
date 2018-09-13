numList = [5,10,15,20,25,30,35,40,45,50]
print(numList)
print(len(numList)) #len is the length and then you chose what list its finding the length of
print(numList[0])

subList1 = numList[0:5]
print(subList1)
subList1.append(30) # .append adds something at the end of the list
print(subList1)

subList2 = numList + [55]
print(subList2)

myClasses = ["AP world","English","spanish","math","python","PE","Bio"]

myClasses.remove("AP world") #have to actually say what you are removing
print(myClasses)
favClasses = myClasses.pop(3) #dont have to say what you are removing, just have to put the place it is in the list.
print(favClasses)



