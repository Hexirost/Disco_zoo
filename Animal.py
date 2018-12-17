from enum import Enum

class Animal():
    def __init__(self, name, pattern, ani_id):
        self.name    = name
        self.pattern = pattern
        self.x       = 0
        self.y       = 0
        self.ani_id  = ani_id
        
    def __repr__(self):
        return self.name
    
    def __str__(self):
        return ( self.name + " X: " + str(self.x) + " Y:" + str(self.y) )
    
class Bestiary(Enum):
    sheep = Animal('sheep',         [(0,0),(0,1),(0,2),(0,3)],  0)
    pig = Animal('pig',             [(0,0),(0,1),(1,0),(1,1)],  1)
    rabbit = Animal('rabbit',       [(0,0),(1,0),(2,0),(3,0)],  2)
    horse = Animal('horse',         [(0,0),(1,0),(2,0)],        3)
    cow = Animal('cow',             [(0,0),(0,1),(0,2)],        4)
    unicorn = Animal('unicorn',     [(0,0),(1,1),(1,2)],        5)
