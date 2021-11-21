import json

class Vertex:
    def __init__(self, x, y):
        if x in range(1,10) and y in range(1,10):
            self.x = x
            self.y = y
    def distance(self, v2):
        return abs(self.x - v2.x) + abs(self.y - v2.y)
    
    def __repr__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y

    def toJSON(self):
        return (self.x,self.y)

    def fromJSON(json_obj):
        return Vertex(json_obj[0], json_obj[1])