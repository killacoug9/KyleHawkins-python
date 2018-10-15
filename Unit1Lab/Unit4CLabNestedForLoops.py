def main():
    for i in range(0,7):
        draw7()


def draw7():
    StarString = '*'
    for xxx in range(0,7):
         StarString += '*'
    print(StarString)

main()

print('\n','space','\n')


#################################



lines =0
while lines < 3:

    print(' *'* 7,end="")
    lines = lines+1
    print('\n',' -'*7)

print('puase')




####################################




def StripeNStar():
    for i in range(3):
        star = ''
        stripe = ''
        for ii in range(7):
            star += ' *'
            stripe += ' -'
        print(star)
        print(stripe)

StripeNStar()



########################################





def incTriangle(num):
    for z in range(num):
        for zz in range(z):
            print(str(z), end='')
        print()


    for j in range(num-2,0,-1):
        for jj in range(j):
             print(str(j), end='')
        print()

incTriangle(10)
