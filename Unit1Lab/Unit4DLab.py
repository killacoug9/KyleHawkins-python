def main():
    shoppingList1 = ['milk', 'toothpaste','Qtips']
    shoppingList2 = ['milk', 'candy', 'apples']
    shoppingList3 = ['paper', 'pencils', 'Qtips']
    shoppingList = [shoppingList1 , shoppingList2 , shoppingList3]
    allInOne(shoppingList)
    milkMilk(shoppingList)
    mooseCookie(shoppingList)
##===========================================================================================================================


def allInOne(ShoppingCart):
    bigList = []
    QtipCount = 0
    for subList1 in ShoppingCart:
        for item in subList1:
            if item == 'Qtips':
                    QtipCount = QtipCount + 1
            if item not in bigList:
                bigList.append(item)

    print('the Qtip count is ' + str(QtipCount))
    print(bigList)

##===========================================================================================================================
##seperate##
##===========================================================================================================================


def milkMilk(ShoppingCart):
    input('now time for challenges baby')

    shoppingList1 = ShoppingCart[0]
    shoppingList2 = ShoppingCart[1]
    shoppingList3 = ShoppingCart[2]
####################
    for z1 in shoppingList1:
        if 'milk' not in shoppingList1:
            shoppingList1.append('milk')
####################
    for z2 in shoppingList1:
        if 'milk' not in shoppingList2:
            shoppingList2.append('milk')
 ###################
    for z3 in shoppingList1:
        if 'milk' not in shoppingList3:
            shoppingList3.append('milk')
#####################
    print(shoppingList1)
    print(shoppingList2)
    print(shoppingList3)

##===========================================================================================================================

def mooseCookie(ShoppingCart):
    input('seperate challenges')

    shoppingList1 = ShoppingCart[0]
    shoppingList2 = ShoppingCart[1]
    shoppingList3 = ShoppingCart[2]
    for item1 in shoppingList1:
        if item1 == 'milk':
            shoppingList1.remove(item1)
            shoppingList1.append('milk and cookies')

    for item2 in shoppingList2:
        if item2 == 'milk':
            shoppingList2.remove(item2)
            shoppingList2.append('milk and cookies')

    for item3 in shoppingList3:
        if item3 == 'milk':
            shoppingList3.remove(item3)
            shoppingList3.append('milk and cookies')
    print(shoppingList1)
    print(shoppingList2)
    print(shoppingList3)




main()

