import sys
from Graph import Graph
from Vertex import Vertex
import copy

def findAdjecentVertexes(g: Graph, v: Vertex) -> list:
    if not v:
        return 
    res = []
    for edge in g.edges:
        if edge.vertex1 == v:
            res.append(edge.vertex2)
        elif edge.vertex2 == v:
            res.append(edge.vertex1)
    return res

def findNonAdjecentVertexes(g: Graph, vertexs: list) -> list:
    res = []

    for in_vertex in vertexs: 
        adjacent_vertexs = findAdjecentVertexes(g, in_vertex) 
        if adjacent_vertexs == None:
            continue 
        for vertex in g.vertexs:
            if vertex not in adjacent_vertexs and vertex not in res:
                res.append(vertex)
                
            elif vertex in adjacent_vertexs and vertex in res:
                res.remove(vertex)
            
            
    
    return res
    
def getMinEdgesVertex(graph: Graph, vertexs: list) -> Vertex:
    if vertexs == []:
        return None
    min_edges_count = len(graph.vertexs)
    min_edges_vertex = None
    for vertex in vertexs:
        current_vertext_edges_count = 0
        for edge in graph.edges:
            if edge.containsVertex(vertex):
                current_vertext_edges_count += 1
        if current_vertext_edges_count < min_edges_count:
            min_edges_count = current_vertext_edges_count
            min_edges_vertex = vertex
    return min_edges_vertex


def calculateMaxIndependetSet(graph: Graph) -> set:
    current_vertex = getMinEdgesVertex(graph, graph.vertexs)
    res = []
    vertexs_to_explore = (findNonAdjecentVertexes(graph, [current_vertex]))
    vertexs_to_explore.remove(current_vertex)
    i= 0
    while True:
        if not vertexs_to_explore:
            break
        current_vertex = getMinEdgesVertex(graph, vertexs_to_explore)
        res.append(current_vertex)
        vertexs_to_explore = findNonAdjecentVertexes(graph, res)
        for vertex in res:
            if vertex in vertexs_to_explore:
                vertexs_to_explore.remove(vertex)
    return res

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage:\npython3 greedy_alg.py graph_vertex_count')
    elif len(sys.argv) == 2:
        total_vertexs = int(sys.argv[1])
        graph = Graph.loadGraph(total_vertexs)
        print(calculateMaxIndependetSet(graph))