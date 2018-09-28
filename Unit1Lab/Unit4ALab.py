stringA = 'ABDACEBAFC'
stringB = ''
for x in stringA:
    if x != 'A' or x != 'B':
        stringB = stringB + x

print(stringB)
