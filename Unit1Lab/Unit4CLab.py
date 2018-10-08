num = input('numbers baby..yeah baby yeah, this is how many numbers you want to input')# this is how many numbers to print
print(num)
numList = []

for i in range(0, int(num)):#this is the highest number
    myNum = int(input(' number please'))
    numList.append(int(myNum))
    print(numList)

total = 0
for i in numList:
    total = total + i
    print('i = ' + str(i))
    print("total = " + str(total))
    input('puase')


average = total/int(num)
print('total ' + str(total) + ' / ' + num)
print(average)

