class Pet:
    pass

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return[pet for pet in Pet.all if pet.owner == self]
        