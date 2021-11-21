# Practical Work Number 1

For this assignmente it was required to build a graph generator with n vertexs and a random number of edges per vertex. The final Challange was to build both and exhaustive and greedy algorithms to find the maximum independent set of a given graph.

## Graph.py:
    This module builds graphs. It is also able to serialize the Vertex and Edge objects to json to save and load them. To create a Graph and see the vertexs and edges sets run:
```
    python3 Graph.py n
```
    This class has 2 methods:
        - saveGraph() ;
        - loadGraph(vertex_count) .
    The latter one trys to open a file ./Graphs/graph_{vertex_count}.json 
## GraphsGenerator.py :
    This script is useful to generate a lot of graphs in one go. The parameter passed, vertex_limit, is the last graph vertex count. It generates all the graphs from 1 vertex to vertex_limit.
    Run:
```
    python3 GraphsGenerator.py n
```

# Algorithms
This modules calculates the maximum independent set of a undirected graph. 
Before using this modules you must generate the graph with the number of vertexs you desire.
The current seed for the random vertexs and random edges per vertex is my University number.
To generate a graph with n vertexs and save it run:
```
    python3 Graph.py -save n
```
After this a file called graph_n.json will appear in a Graphs named dir.

## exaustive__alg.py :
    This is an exaustive search algorith. After generating the graph with n vertexs run:
```
    python3 exhaustive_alg.py n
```

    
    

