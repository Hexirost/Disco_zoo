from Animal import Animal
from Animal import Bestiary

class Zoo():
    def __init__(self):
        self.zoo = []

    def add_animals(self, animal):
        for ani in animal:
            self.zoo.append(Bestiary[ani.lower()].value)

    def __repr__(self):
        animals = []
        for animal in self.zoo:
            #print(animal.name, animal.pattern, animal.ani_id)
            animals.append(animal)
        return repr(animals)

    def __str__(self):
        animals = []
        for animal in self.zoo:
            #print(animal.name, animal.pattern, animal.ani_id)
            animals.append(animal)
        return repr(animals)
    
    def get_animals(self):
        animals = []
        for animal in self.zoo:
            animals.append(animal)
        return animals

    def get_animal(self, animal):
        for ani in self.zoo:
            if str(ani) == animal:
                return animal

