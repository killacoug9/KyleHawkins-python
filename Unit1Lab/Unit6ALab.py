import random
#http://openbookproject.net/thinkcs/python/english3e/dictionaries.html# about directories


def main():
    textStuff()


#
# def searchSystem(searchCode):
#
#


def textStuff():
    WantToMakeInput = 'no'
    KeepGoing = 'yes'

    textCodes = {'tyl':'text you later','gtg':'Get The Grenades','brb':'Better Redistribute Bread','lol':'Lenin our leader', 'omg':'Opponents meet gulag','lmao':'Leninist-Marxist allied operation'}

    while KeepGoing == 'yes':
        searchCode = input('what abbreviation you want, NO CAPS, all undercase')


        if searchCode in textCodes:
            print(textCodes[searchCode])

        else:
            print('sorry i cant find that')
            WhatToDo = input('what do you want to do ')

            if WhatToDo == 'delete':
                delin = input('what abbreviation')
                del textCodes[delin]
            elif WhatToDo == 'change':
                word = input('what is the abbreviation no capitols')
                term = input('what is the saying')
                textCodes[word] = term
                #textCodes.update({word : term})
                print('geez i didnt think of that one')




            # WantToMakeInput = input('would u like to make new option')
            # if WantToMakeInput == 'yes':


            elif WantToMakeInput == 'no':
                print('thats too bad')





        KeepGoing = input('wanna find another abreviation')





main()
