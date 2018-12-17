class Grid():
    def __init__(self, zoo, points = None):

        self.zoo    = zoo
        self.points = points if points else []

    def check(self, curr_grid = []):
        all_points = {}
        for animal in self.zoo:
            for cell in animal.pattern:
                x = cell[0] + animal.x
                y = cell[1] + animal.y
                adj_point = (x,y)
                if int(x) >= 5 or int(y) >= 5:# TODO FIX: hardcoded size of map
                    #print (adj_point)
                    return None
                if adj_point in all_points:
                    #print(adj_point, all_points)
                    return None
                if adj_point in all_points:
                    if animal.name in all_points[adj_point]:
                        all_points[adj_point][animal.name]+=1
                    else:
                        all_points[adj_point][animal.name]=1
                else:
                    all_points[adj_point] = animal.name
        return all_points

