from json.encoder import JSONEncoder
import random
from Vertex import Vertex
from Edge import Edge
import sys
import copy
import json
        
class Graph:
    def __init__(self, total_vertexs:int):
            random.seed(88194)
            self.total_vertexs = total_vertexs
            self.vertexs = self.generateVertexs()
            self.edges = self.generateEdges()

    def saveGraph(self):
        save_file_name = 'Graphs/graph_' + str(self.total_vertexs) + '.json'
        save_file = open(save_file_name, 'w')
        vertex_dump = [v.toJSON() for v in self.vertexs]
        edges_dump = [v.toJSON() for v in self.edges]
        json.dump({'vertexs': vertex_dump, 'edges': edges_dump}, save_file)
        
    def loadGraph(vertex_count: int):
        save_file_name = 'Graphs/graph_' + str(vertex_count) + '.json'
        save_file = open(save_file_name, 'r')
        context = json.load(save_file)
        res = Graph(0)
        res.total_vertexs = vertex_count
        res.vertexs = [Vertex.fromJSON(v) for v in context['vertexs']]
        res.edges = [Edge.fromJSON(e) for e in context['edges']]
        return res
        


    def generateEdges(self):
        edges = []
        for vertex in self.vertexs:
            current_vertex_edges = 0
            for edge in edges:
                if edge.containsVertex(vertex):
                    current_vertex_edges += 1
            max_edges_to_insert = self.total_vertexs - current_vertex_edges
            vertex_edges = random.randint(0, max_edges_to_insert)
            for i in range(vertex_edges):
                to_insert = self.generateEdge(vertex, edges)
                if to_insert:
                    edges.append(to_insert)
                else:
                    break
        return edges

    def generateEdge(self, vertex, edges):
        potential_vertexs = copy.deepcopy(self.vertexs)
        potential_vertexs.remove(vertex)
        for edge in edges:
            if vertex == edge.vertex1:
                potential_vertexs.remove(edge.vertex2)
            elif vertex == edge.vertex2:
                potential_vertexs.remove(edge.vertex1)
        if len(potential_vertexs) != 0:
            rand_vertex = random.randint(0, len(potential_vertexs)-1)
            return Edge(vertex, potential_vertexs[rand_vertex])
        else:
            return None


    def generateVertexs(self):
        inserted_vertexs = 0
        vertexs = []
        while(inserted_vertexs != self.total_vertexs): 
            x = random.randint(1, 9)
            y = random.randint(1, 9)
            to_insert = Vertex(x,y)
            if self.checkValidVertex(to_insert, vertexs):
                vertexs.append(to_insert)
                inserted_vertexs += 1
        return vertexs
        

    def checkValidVertex(self, to_insert, vertexs):
        for vertex in vertexs:
            if to_insert.distance(vertex) <= 1:
                return False
        return True



if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage:\npython3 Graph.py vertex_count')
    elif len(sys.argv) == 2:
        total_vertexs = int(sys.argv[1])
        graph = Graph(total_vertexs)
        print(graph.vertexs)
        print(graph.edges)