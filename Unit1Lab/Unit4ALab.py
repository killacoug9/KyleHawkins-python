

def main():
    ye = input('whaqts urotyu9 sring ')
    print(ye)
    print(deVowel(ye))


def deVowel(ye):
    noVowel = ''
    for x in ye:
        if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
            y =4000
        else:
            noVowel = noVowel + x
    return (noVowel)


main()
for i in range(0,5):
    print(i)
