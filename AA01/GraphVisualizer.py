import numpy
import sys
from Graph import Graph
import matplotlib.pyplot as plt
from exhaustive_alg import calculateMaxIndependetSet as exaustive_alg
from greedy_alg import calculateMaxIndependetSet as greedy_alg

def showMaximumIndependetSet(maximum_indepedent_set : list):
  points = []
  for vertex in maximum_independet_set:
    points.append([vertex.x, vertex.y])
  points = numpy.array(points)
  x = points[:, 0].flatten()
  y = points[:, 1].flatten()
  plt.plot(x, y, color="red", linestyle='--',markerfacecolor='y', marker='o')
  plt.show()

def showGraph(graph : Graph):
  points = []
  for vertex in graph.vertexs:
    points.append([vertex.x, vertex.y])
  edges = []
  for edge in graph.edges:
    edges.append([graph.vertexs.index(edge.vertex1), graph.vertexs.index(edge.vertex2)])
  points = numpy.array(points)
  edges = numpy.array(edges)
  x = points[:, 0].flatten()
  y = points[:, 1].flatten()

  plt.plot(x[edges.T], y[edges.T], linestyle='-', color='black',
          markerfacecolor='y', marker='o')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage:\npython3 GraphVisualizer.py vertex_count (exhaustive|greedy)')
    elif len(sys.argv) == 3:
        total_vertexs = int(sys.argv[1])
        graph = Graph.loadGraph(total_vertexs)
        if sys.argv[2] == "exhaustive":
            maximum_independet_set = exaustive_alg(graph)
            showGraph(graph)
            showMaximumIndependetSet(maximum_independet_set)
        elif sys.argv[2] == "greedy":
            maximum_independet_set = greedy_alg(graph)
            showGraph(graph)
            showMaximumIndependetSet(maximum_independet_set)
        else:
            print("The algorith must be either exhaustive or greedy!")
        
