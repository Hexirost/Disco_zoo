import random
import numpy as np
import collections

from Animal import Animal
from Animal import Bestiary
from Zoo import Zoo
from Grid import Grid

X = 5
Y = 5
X-=1
Y-=1
#TODO UGLY FIX CODE

DEFAULT_MAP = [[0]*(X) for i in range(Y)]

def check():
    return True

#TODO ADD ZONES
animals = "horse rabbit" #input("Animals: ")
map_animals = animals.split(" ")
num_animals = len(map_animals)

zoo = Zoo()
for animal in map_animals:
    zoo.add_animals([animal])

grid = Grid(zoo.get_animals())

freq_map = [ [{} for j in range(X+1)] for i in range(Y+1)]

## TODO IMPLEMENT VALID LOCATIONS for each animals as a method to generate list of all valid points
animal_info  = zoo.get_animals() 
animal_index = num_animals - 1
current_map = np.copy(DEFAULT_MAP)
count = 0
valid = 0

while animal_info[0].x != X+1:
    curr_animal = animal_info[animal_index]

    if count:
        curr_animal.y += 1

    if curr_animal.y > Y:
        curr_animal.y = 0
        curr_animal.x += 1
        if curr_animal.x > X:
            if animal_index == 0:
                break
            else:
                curr_animal.x = 0
                curr_animal.y = -1
                animal_index -= 1
                continue
    
    count += 1
    # print(str(count), ". ",end = "")
    # for ani in animal_info:
    #     print(ani,end="\t")
    # print()
    
    if animal_index == num_animals-1:
        check = grid.check(current_map)
        if check:
            valid += 1
            for key in check:

                if check[key] in freq_map[key[0]][key[1]]:
                    freq_map[key[0]][key[1]][check[key]] += 1
                else:
                    freq_map[key[0]][key[1]][check[key]]  = 1
                    
    else:
        animal_index += 1
        
for ele in freq_map:
    for cell in ele:
        for ani in cell:
            print(ani,"{0:4.0%}".format(cell[ani]/valid),end = " ")
        print("|",end = "")
    print()
    