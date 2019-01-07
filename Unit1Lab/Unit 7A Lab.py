import Unit7Classes as c

d = c.pet('300', 'jamal', 'pitbull')
print(c.pet.what(d))
print(c.pet.getName(d))
print(c.pet.getBreed(d) + '\n')

g = c.pet('∞', 'Apyr', 'persian')
print(c.pet.getName(g))
print(c.pet.getBreed(g))
print(c.pet.what(g) + '\n')

h = c.cage('wolverine', 'True')
print(c.cage.getBreed(h))
print(c.cage.getDanger(h))
print(c.cage.what(h) + '\n')

j = c.cage('Macaw', 'False')
print(c.cage.getBreed(j))

print(c.cage.getDanger(j))
print(c.cage.what(j))
