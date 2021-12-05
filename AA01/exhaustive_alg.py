import sys
from Graph import Graph
from Vertex import Vertex
import copy
comps = 0

def findAdjecentVertexes(g: Graph, v: Vertex) -> list:
    global comps
    res = []
    for edge in g.edges:
        comps += 2
        if edge.vertex1 == v:
            res.append(edge.vertex2)
        elif edge.vertex2 == v:
            res.append(edge.vertex1)
    return res

def findNonAdjecentVertexes(g: Graph, v: Vertex) -> list:
    global comps
    adjacent_vertexs = findAdjecentVertexes(g, v) 
    #Just by checking the vertexes not connected to v 
    #(the same code as findAdjacentVertexs but only appending on the else condition) in the edges list
    #you might not get all the vertexes that are non adjacent, since they might no be in the edges.
    res = []
    for vertex in g.vertexs: 
        if vertex not in adjacent_vertexs:
            comps += 1
            res.append(vertex)
    to_remove = []
        
    if len(res) > 1:
        comps += 1
        end = len(res)-1
        for j in range(int(end)):
            for i in range(j, end):
                adjacent_vertexs = findAdjecentVertexes(g, res[i])
                if res[j] in adjacent_vertexs:
                    if res[j] not in to_remove:
                        comps += 2
                        to_remove.append(res[j])
                    
    for rem in to_remove:
        res.remove(rem)
    return res

def calculateMaxIndependetSet(graph: Graph) -> set:
    global comps

    vertexs_half = int((graph.total_vertexs + 1) / 2) #No need to check past half of the number of vertexes.
    res = []
    for i in range(vertexs_half):
        non_adjacent_vertexs = findNonAdjecentVertexes(graph, graph.vertexs[i])
        #this list includesgraph.vertexs[i]         
        if len(non_adjacent_vertexs) > len(res):
            comps += 1
            res = copy.deepcopy(non_adjacent_vertexs)
    return res

def getComps():
    global comps
    return comps

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage:\npython3 exhaustive_alg.py graph_vertex_count')
    elif len(sys.argv) == 2:
        total_vertexs = int(sys.argv[1])
        graph = Graph.loadGraph(total_vertexs)
        print(calculateMaxIndependetSet(graph))
        print("comparations: " + str(comps))