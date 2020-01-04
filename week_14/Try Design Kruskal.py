from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices
        self.graph1 = defaultdict(int)
        
    def addEdge(self,u,v,w):        
        self.graph1[str(u) + "-" + str(v)] = w    
    
    def Kruskal(self):            
        sort_graph = sorted(self.graph1.items(), key=lambda graph1: graph1[1])
        
        if len(sort_graph) < self.V-1:
            return
        
        src = []
        dest = []
        weight = []
        
        for i in range(len(sort_graph)):
            src.append(int(sort_graph[i][0].split('-')[0]))
            dest.append(int(sort_graph[i][0].split('-')[1]))
            weight.append(int(sort_graph[i][1]))

        root = [-1]*self.V
        edge = []
        j = 0
    
        while len(edge) < self.V-1:
            if root[dest[j]] == -1:
                if root[src[j]] != -1:  # 起點本身有別的root的，要將終點放到src的root內
                    root[dest[j]] = root[src[j]]
                    for k in range(root.count(dest[j])):     # 原本為root
                        root[root.index(dest[j])] = root[src[j]]
                else:
                    root[dest[j]] = src[j]
                    for k in range(root.count(dest[j])):     # 原本為root
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
                    for k in range(root.count(root[dest[j]])):
                        root[root.index(root[dest[j]])] = root[src[j]]
                    root[root[dest[j]]] = root[src[j]]
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
        min_cost = 0
        for l in edge:
            MST[sort_graph[l][0]] = sort_graph[l][1]
            min_cost += weight[l]
        
        return min_cost, MST
