# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 

from collections import defaultdict 

# This class represents a directed graph 
# using adjacency list representation 
class Graph:
    # Constructor 
    def __init__(self):
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
    
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        
    def _key_value(self, key, method, temp):
        value = self.graph[key]

        for i in value:
            if not (i in temp):
                method.append(i)
                temp.append(i)

        return method, temp
    
    # Function to print a BFS of graph 
    def BFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        temp = [s]
        bfs = [s]
        queue = []

        queue, temp = self._key_value(s, queue, temp)

        while queue:
            queue, temp = self._key_value(queue[0], queue, temp)

            bfs.append(queue.pop(0))

        return bfs
        
        
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        temp = [s]
        dfs = [s]
        stack = []

        stack, temp = self._key_value(s, stack, temp)

        while stack:
            tempp = stack.pop()
            dfs.append(tempp)

            stack, temp = self._key_value(tempp, stack, temp)

        return dfs
   
