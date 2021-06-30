from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def DFSUtil(self,v,visited):
        visited.add(v)
        print(v,end=" ")

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour,visited)


    def DFS(self,v):

        visited =set()
        print("The DFS traversal is as follows: ")
        self.DFSUtil(v,visited)

MyGraph= Graph()
MyGraph.addEdge(0,1)
MyGraph.addEdge(0,2)
MyGraph.addEdge(1,2)
MyGraph.addEdge(2,0)
MyGraph.addEdge(2,3)
MyGraph.addEdge(3,3)

MyGraph.DFS(2)