class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Owner name must be a string.")
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self ]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet.")
        pet.owner = self

    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string.")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Pet type '{pet_type}' is not available.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)
    