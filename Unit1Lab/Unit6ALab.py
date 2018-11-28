import random
#http://openbookproject.net/thinkcs/python/english3e/dictionaries.html# about directories


def main():
    textStuff()


#
# def searchSystem(searchCode):
#
#


def textStuff():
    KeepGoing = 'yes'
    while KeepGoing == 'yes':
        searchCode = input('what abbreviation you want')
        textCodes = {'tyl':'text you later','gtg':'Get The Grenades','brb':'Better Redistribute Bread','LOL':'Lenin our leader', 'OMG':'Opponents meet gulag','LMAO':'Leninist-Marxist allied operation'}


        if searchCode in textCodes:
            print(textCodes[searchCode])
        else:
            WantToMakeInput = input('would u like to make new option')

        if WantToMakeInput == 'yes':
            print('ok')
        elif WantToMakeInput == 'no':
            print('thats too bad')

        KeepGoing = input('wanna find another abreviation')






    #
    # searchCode = input('what abbreviation you want')
    # textCodes = {'tyl':'text you later','gtg':'Get The Grenades','brb':'Better Redistribute Bread','LOL':'Lenin our leader', 'OMG':'Opponents meet gulag','LMAO':'Leninist-Marxist allied operation'}
    #
    #


    #
    # if searchCode in textCodes:
    #      print(textCodes[searchCode])
    # else:
    #     WantToMakeInput = input('would u like to make new option')
    #
    # if WantToMakeInput == 'yes':
    #     print('ok')
    #















main()
