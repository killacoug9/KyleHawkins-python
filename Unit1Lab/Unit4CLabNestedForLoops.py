def main():
    for i in range(0,7):
        draw7()


def draw7():
    StarString = '*'
    for xxx in range(0,7):
         StarString += '*'
    print(StarString)

main()

print('space')

def main2():

    stars = '*'

    for i in range(0,7):

        print(stars, end="")
        StarsAndStripes()


def StarsAndStripes():
    stripes = '-'
    for i in range(0,7):
        print(stripes, end='')



main2()
