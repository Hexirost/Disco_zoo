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
DEFAULT_MAP = [[0]*(X) for i in range(Y)]

def check():
    return True

#zone    = input("Map: ")
animals = "sheep cow pig" #input("Animals: ")
map_animals = animals.split(" ")
num_animals = len(map_animals)

zoo = Zoo()
for animal in map_animals:
    zoo.add_animals([animal])

grid = Grid(zoo.get_animals())

freq_map = [ [{} for j in range(X+1)] for i in range(Y+1)]
#freq_map = [ [[float("%0.2f"%0.00)] for j in range(X+1)] for i in range(Y+1)]
print(freq_map)
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
    print(str(count), ". ",end = "")
    for ani in animal_info:
        print(ani,end="\t")
    print()
    
    if animal_index == num_animals-1:
        check = grid.check(current_map)
        if check:
            print("CHECK: ",check,)
            valid += 1
            for key in check:
                # print("KEY", key,check[key])
                # print(freq_map[key[0]][key[1]])
                # print(check[key])
                if check[key] in freq_map[key[0]][key[1]]:
                    freq_map[key[0]][key[1]][check[key]] += 1
                else:
                    freq_map[key[0]][key[1]][check[key]]  = 1
                # print("Key:", key)
                # if key in grid_dict:
                #     grid_dict[key]+= 1
                # else:
                #     grid_dict[key] = 1
    else:
        animal_index += 1
#          [el for el in X if not isinstance(el, str)]

for ele in freq_map:
    print(ele)
    # print(str(count), ". ",end = "")
    # for ani in animal_info:
    #     print(ani,end="\t")
    # print(animal_index)

    # for col in current_map:
    #     for cell in col:
    #         print(cell,end="   ")
    #     print()
    # for animal in zoo.get_animals():
    #     pattern = animal.pattern
    

# count = 0
# # print out frequency map
# for col in freq_map:
#     for cell in col:
#         # cell[0] += 1 + count
#         # cell[1] += 2 + count
#         # cell[2] += 3 + count
#         # count += 1
#         print(cell,end="   ")
#     print()
