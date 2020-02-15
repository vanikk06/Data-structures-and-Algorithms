from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.dict = defaultdict(list) 
        
    def addEdge(self,u,v,w): 
        self.dict[w].append([u,v])
        
    def Dijkstra(self, s): 
        nodes=[]
        for i in range(self.V):
            nodes.append(i)
            
        seen=[] 
        distance={s:0}  
        result={}
        
        for i in nodes:
            distance[i]=self.graph[s][i]
    
        for i in distance:
            if distance[i]>0:
                seen.append(i)
        nodes.remove(s)
        for v in seen:
            for d in nodes:
                new = self.graph[s][v]+self.graph[v][d]
                if  self.graph[s][v] is not 0 and self.graph[v][d] is not 0:
                    if distance[d]==0 or new < distance[d]:
                        self.graph[s][d]=new
                        distance[d]=new
                        seen.append(d)

        for x in range(self.V):
            result[str(x)]=distance[x]

        return result
    
    def Kruskal(self):
        seen=[]
        for i in range(self.V):
            seen.append(i)
            
        result={}
        for i in sorted(self.dict):
            for j,k in self.dict[i]:
                if seen[j] == seen[k]:
                    pass
                else:
                    seen = [seen[j] if x==seen[k] else x for x in seen]
                    result[str(j)+'-'+str(k)] = i
        return result
        
# By 朱宣霓
## Github：https://github.com/pignini/as
