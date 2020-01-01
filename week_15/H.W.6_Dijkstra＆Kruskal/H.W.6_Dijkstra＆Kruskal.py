# Python program for Dijkstra's single  
# source shortest path algorithm. The program is  
# for adjacency matrix representation of the graph 
# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected,  
# undirected and weighted graph 

from collections import defaultdict

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []
        self.graph1 = defaultdict(int)
        self.graph_matrix = [[-1 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        
        self.graph1[str(u) + "-" + str(v)] = w
        
    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
        min_cost = None
        fix_min_index = None
        fix_time = 0
        checked = [s]

        for i in range(self.V):
            self.graph_matrix[s][s] = 0
            if self.graph[s][i] != 0:  # 排除自己的情況
                self.graph_matrix[s][i] = self.graph[s][i]
                if not min_cost:
                    min_cost = self.graph[s][i]
                if min_cost > self.graph[s][i]:
                    min_cost = self.graph[s][i]
        
        while len(checked) < self.V:
            min_index = self.graph_matrix[s].index(min_cost)
            while min_index in checked:
                if not fix_min_index:
                    fix_min_index = self.graph_matrix[s].copy()
                
                fix_min_index.remove(min_cost)
                fix_time += 1
                min_index = fix_min_index.index(min_cost) + fix_time          

            checked.append(min_index)
            self.graph_matrix[min_index] = self.graph_matrix[s].copy()
            for j in range(self.V):
                if j in checked:
                    continue
                if self.graph[min_index][j] != 0:
                    if self.graph_matrix[s][j] == -1:  #原本沒連結
                        self.graph_matrix[min_index][j] = self.graph_matrix[s][min_index] + self.graph[min_index][j]
                    else:
                        if self.graph_matrix[s][min_index] + self.graph[min_index][j] < self.graph_matrix[s][j]:
                            self.graph_matrix[min_index][j] = self.graph_matrix[s][min_index] + self.graph[min_index][j]

            if len(checked) < self.V:                 #找min_cost
                temp = []
                for k in range(self.V):
                    if k not in checked and self.graph_matrix[min_index][k] != -1:
                        temp.append(self.graph_matrix[min_index][k])

                min_cost = min(temp)
        
            s = min_index    
        
        SP = {}
        for m in range(self.V):
            SP[str(m)] = self.graph_matrix[min_index][m]
            
        return SP
    
    
    def Kruskal(self):
        """
        :rtype: dict
        """       
        sort_graph = sorted(self.graph1.items(), key=lambda graph1: graph1[1])
        
        if len(sort_graph) < self.V-1:
            return
        
        src = []
        dest = []
        
        for i in range(len(sort_graph)):
            src.append(int(sort_graph[i][0].split('-')[0]))
            dest.append(int(sort_graph[i][0].split('-')[1]))

        root = [-1]*self.V
        edge = []
        j = 0
    
        while len(edge) < self.V-1:
            if root[dest[j]] == -1:
                if root[src[j]] != -1:  # 起點本身有別的root的，要將終點放到src的root內
                    if root[dest[j]] == src[j] or root[dest[j]] == root[src[j]]:    # 排除cycle
                        j += 1
                        continue
                    root[dest[j]] = root[src[j]]
                else:
                    root[dest[j]] = src[j]
                    for k in range(root.count(dest[j])):     # 原本為root的連到別的root
                        root[root.index(dest[j])] = src[j] 
                edge.append(j)
            elif root[dest[j]] == src[j] or root[dest[j]] == root[src[j]]:
                j += 1
                continue
            else:
                if root[src[j]] != -1:
                    if root[dest[j]] == root[src[j]] or root[dest[j]] == src[j]: # 排除cycle
                        j += 1
                        continue
                    temp = root[dest[j]]
                    for k in range(root.count(temp)):
                        root[root.index(temp)] = root[src[j]]
                    root[temp] = root[src[j]]
                    edge.append(j)
                else:
                    if root[dest[j]] == root[src[j]] or root[dest[j]] == src[j]: # 排除cycle
                        j += 1
                        continue                    
                    root[root[dest[j]]] = src[j]
                    for k in range(root.count(root[dest[j]])):
                        root[root.index(root[dest[j]])] = src[j]  
                    edge.append(j)

            j += 1
            
        MST = {}
        for l in edge:
            MST[sort_graph[l][0]] = sort_graph[l][1]
        
        return MST
