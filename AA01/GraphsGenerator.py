import sys
from Graph import Graph 



if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage:\npython3 GraphsGenerator.py vertex_limit\n\tvertex_limit: Generate graphs with 1 vertex to vertex_limit vertexs')
    elif len(sys.argv) == 2:
        vertex_limit = int(sys.argv[1])
        for i in range(1, vertex_limit + 1):
            Graph(i).saveGraph()
