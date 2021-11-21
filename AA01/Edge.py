import json

from Vertex import Vertex
class Edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    def containsVertex(self, vertex):
        if vertex == self.vertex1 or vertex == self.vertex2:
            return True
        return False
    
    def __repr__(self) -> str:
        return str(self.vertex1) + '--' + str(self.vertex2)

    def toJSON(self):
        return (self.vertex1.toJSON(),self.vertex2.toJSON())
    
    def fromJSON(json_obj):
        return Edge(Vertex.fromJSON(json_obj[0]), Vertex.fromJSON(json_obj[1]))