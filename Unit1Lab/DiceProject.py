import random
for x in range(1):
  print(random.randint(1,6))



def main():
    decision = input('do u wanna keep going')
    if decision == "y":
        counter = True
    else:
        counter = False

createDie()
interactions()

def createDie():
