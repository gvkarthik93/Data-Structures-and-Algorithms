# Python program to print DFS traversal from a
# given given graph
from collections import defaultdict
 
# This class represents a directed graph using
# adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # A function used by DFS
    def DFSUtil(self,node, recursionStack, visited):
 
        # Mark the current node as visited and print it
        visited[node]= True
        recursionStack.add(node)
 
        # Recur for all the vertices adjacent to this vertex
        for child in self.graph[node]:
            if visited[child] == False:
                if self.DFSUtil(i, recursionStack, visited):
                    return True
            elif child in recursionStack:
                return True

        recursionStack.remove(node)
        return False
 
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self):
        # Mark all the vertices as not visited
        visited = [False]*(len(self.graph))
        recursionStack = set()
 
        # Call the recursive helper function to print
        # DFS traversal
        for node in self.graph:
            if visited[node] == False:
                if self.DFSUtil(node, recursionStack, visited):
                    return True

        return False
 
 
# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# Returns true if there's a cycle in graph
print (g.dfs())