numList = [5,10,15,20,25,30,35,40,45,50] # needs to be brackets
print(numList)
print(len(numList)) #len is the length/how mny charcters are in the list, and then you chose what list its finding the length of
print(numList[0]) #gives you the first number in the list which is 5

subList1 = numList[0:5] #makes a sub list that in
print(subList1)
subList1.append(30) # .append adds something at the end of the list
print(subList1) #PRINTS THE SUB LIST

subList2 = numList + [55]
print(subList2)

myClasses = ["AP world","English","spanish","math","python","PE","Bio"]

myClasses.remove("AP world") #have to actually say what you are removing
print(myClasses)
favClasses = myClasses.pop(3) #dont have to say what you are removing, just have to put the place it is in the list.
print(favClasses)



