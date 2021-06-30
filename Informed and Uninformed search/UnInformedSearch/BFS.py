from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def BFS(self,v):
        print("The BFS traversal of the given graph is as follows: ")
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(v)
        visited[v] = True

        while queue:
            v = queue.pop(0)
            print(v, end = " ")
            for neighbour in self.graph[v]:
                if visited[neighbour] == False:
                    queue.append(neighbour)
                    visited[neighbour] = True

MyGraph= Graph()
MyGraph.addEdge(0,1)
MyGraph.addEdge(0,2)
MyGraph.addEdge(1,2)
MyGraph.addEdge(2,0)
MyGraph.addEdge(2,3)
MyGraph.addEdge(3,3)

MyGraph.BFS(2)