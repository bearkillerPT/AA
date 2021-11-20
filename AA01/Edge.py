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