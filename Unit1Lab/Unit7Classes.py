
class pet:
    petType = 'cage free pet'
    def __init__(self, age, name, breed):
        self.age = age
        self.name = name
        self.breed = breed

    def getAge(self):
        return(self.age)

    def getBreed(self):
        return(self.breed)

    def getName(self):
        return(self.name)

    def what(self):
        return('This is a '+ self.petType + ' who is ' + self.age + ' years old, it is a ' + self.breed + ' named ' + self.name + '.')


class cage:
    petType = 'caged pet'
    def __init__(self, breed, danger):
        self.breed = breed
        self.danger = danger

    def getDanger(self):
        return(self.danger)

    def getBreed (self) :
        return(self.breed)

    def calcDang (self) :
        if self.danger=='True' :
            return('is highly dangerous.')
        elif self.danger=='False' :
            return('isnt dangerous, or is it???.')

    def what(self):
        return('This is a '+ self.petType + ' who is a ' + self.breed + ' and ' + self.calcDang())




class dog(pet):
    def __init__(self, age, name, breed, activity):

        pet.__init__(self, age, name, breed)

        self.activity = activity

    def info (self) :
        return('This is a '+ self.petType + ' who is ' + self.age + ' years old, is a ' + self.breed + ' named ' + self.name + ' who is currently ' + self.activity + '.')


class pet1(pet):
    def __init__(self,name,breed):

        pet.__init__('20','',name,breed)

    def info(self):

        return('This is a '+ self.petType + ' who is ' + self.age + ' years old, is a ' + self.breed + ' named ' + self.name + ' who is currently ' + self.activity + '.')

