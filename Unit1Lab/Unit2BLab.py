#x = int(input("enter a negative or positive number"))
#if x >= 0:
#    print("x is positive")
#elif x < 0:
#    print("x is negative")


numGrade = int(input("input number grade"))
print(numGrade)

if numGrade >= 90:
    print("yahoo")
elif numGrade >= 80:
    print("you got a B")
elif numGrade >= 70:
    print("you got a C")
else:
    print("you better study harder")

userInput = str(input("type favorite color"))
print(userInput)
print("i like " + userInput + " too -computer")

color = userInput
if color == "blue":
    print("the sky is blue")
elif color == "green":
    print("the forest is green")
elif color == "red":
    print("I LOVE RED")
elif color == "yellow":
    print("yuck yellow")
else:
    print("i am dumb computer who only knows 4 colors")

