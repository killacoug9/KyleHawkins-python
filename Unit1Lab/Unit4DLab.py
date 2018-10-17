def main():
    shoppingList1 = ['milk', 'toothpaste','Qtips']
    shoppingList2 = ['milk', 'candy', 'apples']
    shoppingList3 = ['paper', 'pencils', 'Qtips']
    shoppingList = [shoppingList1 , shoppingList2 , shoppingList3]
    allInOne(shoppingList)





def allInOne(ShoppingCart):
    bigList = []
    QtipCount = 0
    for subList1 in ShoppingCart:
        for item in subList1:
            if item == 'Qtips':
                    QtipCount = QtipCount + 1
            if item not in bigList:
                bigList.append(item)

    print(QtipCount)
    print(bigList)



main()

