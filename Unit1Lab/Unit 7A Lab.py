




class pet():
    petType = 'cage free pet'

    def __init__(self, type, name, breed):
        self.type = type
        self.name = name
        self.breed = breed

    def getType(self):
        return(self.type)

    def getBreed(self):
        return(self.breed)

    def getName(self):
        return(self.name)

    def whatIsIt(self):
        return('This is a ' + self.petType + ' years old, is a ' + self.breed + ' named ' + self.name + '.')









class cage():

    petType = 'caged pet'

    def __init__(self, Type, danger):
        self.Type = Type
        self.danger = danger

    def getDanger(self):
        return(self.danger)

    def getBreed (self) :
        return(self.Type)

    def whatDanger (self) :
        if self.danger=='True' :
            return('is dangerous.')

        elif self.danger=='False' :
            return('isnt dangerous.')

    def what(self):
        return('This is a ' + self.petType + ' who is a ' + self.Type + ' and ' + self.whatDanger())





