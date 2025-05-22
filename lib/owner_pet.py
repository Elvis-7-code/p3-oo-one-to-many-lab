class Pet:
    pass

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return[pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("add_pet argument must be an instance of Pet")
        pet.owner =self
    
    