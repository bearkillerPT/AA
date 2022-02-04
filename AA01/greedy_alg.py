import sys
from Graph import Graph
from Vertex import Vertex
comps = 0


def findAdjecentVertexes(g: Graph, v: Vertex) -> list:
    global comps
    if not v:
        comps += 1
        return 
    res = []
    for edge in g.edges:
        comps += 2
        if edge.vertex1 == v:
            res.append(edge.vertex2)
        elif edge.vertex2 == v:
            res.append(edge.vertex1)
    return res

def findNonAdjecentVertexes(g: Graph, vertexs: list) -> list:
    global comps

    res = []

    for in_vertex in vertexs: 
        adjacent_vertexs = findAdjecentVertexes(g, in_vertex) 
        if adjacent_vertexs == None:
            comps += 1
            continue 
        for vertex in g.vertexs:
            if vertex in res:
                if vertex in adjacent_vertexs:
                    res.remove(vertex)
                    comps += 2

            else:
                if vertex not in adjacent_vertexs:
                    if vertex not in vertexs:
                        res.append(vertex)
                        comps += 3
    return res
    
def getMinEdgesVertex(graph: Graph, vertexs: list) -> Vertex:
    global comps
    if vertexs == []:
        comps += 1
        return None
    min_edges_count = len(graph.vertexs)
    min_edges_vertex = None
    for vertex in vertexs:
        current_vertext_edges_count = 0
        for edge in graph.edges:
            if edge.containsVertex(vertex):
                comps += 2
                current_vertext_edges_count += 1
        if current_vertext_edges_count < min_edges_count:
            comps += 1
            min_edges_count = current_vertext_edges_count
            min_edges_vertex = vertex
    return min_edges_vertex


def calculateMaxIndependetSet(graph: Graph) -> set:
    global comps

    current_vertex = getMinEdgesVertex(graph, graph.vertexs)
    res = []
    vertexs_to_explore = (findNonAdjecentVertexes(graph, [current_vertex]))
    res.append(current_vertex)
    while True:
        if not vertexs_to_explore:
            comps += 1
            break
        current_vertex = getMinEdgesVertex(graph, vertexs_to_explore)
        res.append(current_vertex)
        vertexs_to_explore = findNonAdjecentVertexes(graph, res)
    return res

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage:\npython3 greedy_alg.py graph_vertex_count')
    elif len(sys.argv) == 2:
        total_vertexs = int(sys.argv[1])
        graph = Graph.loadGraph(total_vertexs)
        print(calculateMaxIndependetSet(graph))
        print(comps)