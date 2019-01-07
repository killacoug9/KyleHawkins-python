import Unit7Classes as c

d = c.pet('300', 'jamal', 'pitbull')

print(c.pet.getName(d))

print(c.pet.getBreed(d) + '\n')


########
d = c.dog('300','jamal','pitbull','cruzin down the street in his six,four')

print(c.dog.info(d) + '\n')
