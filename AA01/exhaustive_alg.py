import sys
from Graph import Graph
from Vertex import Vertex
import copy

def findAdjecentVertexes(g: Graph, v: Vertex) -> list:
    res = []
    for edge in g.edges:
        if edge.vertex1 == v:
            res.append(edge.vertex2)
        elif edge.vertex2 == v:
            res.append(edge.vertex1)
    return res

def findNonAdjecentVertexes(g: Graph, v: Vertex) -> list:
    adjacent_vertexs = findAdjecentVertexes(g, v) 
    #Just by checking the vertexes not connected to v 
    #(the same code as findAdjacentVertexs but only appending on the else condition) in the edges list
    #you might not get all the vertexes that are non adjacent, since they might no be in the edges.
    res = []
    for vertex in g.vertexs: 
        if vertex not in adjacent_vertexs:
            res.append(vertex)
    if len(res) > 1:
        for j in range(len(res) - 1):
            for i in range(j, len(res)-1):
                adjacent_vertexs = findAdjecentVertexes(g, res[j])
                if res[i] in adjacent_vertexs:
                    res.remove(res[i])
        
    return res

def calculateMaxIndependetSet(graph: Graph) -> set:
    vertexs_half = int((graph.total_vertexs + 1) / 2) #No need to check past half of the number of vertexes.
    res = []
    for i in range(vertexs_half):
        non_adjacent_vertexs = findNonAdjecentVertexes(graph, graph.vertexs[i])
        #this list includesgraph.vertexs[i]         
        if len(non_adjacent_vertexs) > len(res):
            res = copy.deepcopy(non_adjacent_vertexs)
    return res

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage:\npython3 exhaustive_alg.py graph_vertex_count')
    elif len(sys.argv) == 2:
        total_vertexs = int(sys.argv[1])
        graph = Graph.loadGraph(total_vertexs)
        print(calculateMaxIndependetSet(graph))