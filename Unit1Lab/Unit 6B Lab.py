
def main():
    findMonth()

def findMonth():


    weekends = {'Jan':['6','7','13','14','20','21','27','28'],
                'Feb':['3','4','10','11','17','18','24','25'],
                'Mar':['3','4','10','11','17','18','24','25','31'],
                'Apr':['1','7','8','14','15','21','22','28','29'],
                'May':[5,6,12,13,19,20,26,27],
                'Jun':[2,3,9,10,16,17,23,24,30],
                'Jul':[1,7,8,14,15,21,22,28,29],
                'Aug':[4,5,11,12,18,19,25,26],
                'Sep':[1,2,8,9,15,16,22,23,29,30],
                'Oct':[6,7,13,14,20,21,27,28],
                'Nov':[3,4,10,11,17,18,24,25],
                'Dec':['1','2','8','9','15','16','22','23','29','30']

    }
    # for z in BMonth:
    #     if BMonth in weekends:
    #         for x in weekends[BMonth]:
    #             if BDay in weekends[BMonth]:
    #                 print('oh i found it ')
    #                 print('ok')
    # else:
    #     print('sorry i cant find it')
    #

    BMonth = input('what month is ur bday use abreviation')

    formatMonth = ''
    if BMonth == 'Apr':
        formatMonth = '04'
    elif BMonth == 'Jan':
        formatMonth = '01'
    elif BMonth == 'Feb':
        formatMonth = '02'
    elif BMonth == 'Mar':
        formatMonth = '03'






    if BMonth in weekends:
        BDay = input('what is the day')
        if BDay in weekends[BMonth]:
            print('oh noce you bday is on the weekend ' + formatMonth +' / '+ BDay + ' / ' + '2018')
    else:
        print('sorry i cant find that month')

#print("\033[1;32; Bright Green")




main()
