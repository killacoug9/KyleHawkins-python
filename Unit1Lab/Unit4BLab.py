def numberOne():
    numbers = []
    for i in range(1,6):
        numbers.append(i + 10)
        numbers.append(i * 10)
    print(numbers)




def numberTwo():

    numbers2 = [10,20,30,40,50]

    for x in range(len(numbers2)):
        numbers2[x] =numbers2[x]*10


    print(numbers2)




numberOne()
input("pause")
numberTwo()
