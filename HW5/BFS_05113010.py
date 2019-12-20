from collections import defaultdict 
  
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        
    def _key_value(self, key, method, temp):
        value = self.graph[key]

        for i in value:
            if not (i in temp):
                method.append(i)
                temp.append(i)

        return method, temp
  
    def BFS(self, s): 
        temp = [s]
        bfs = [s]
        queue = []

        queue, temp = self._key_value(s, queue, temp)

        while queue:
            queue, temp = self._key_value(queue[0], queue, temp)

            bfs.append(queue.pop(0))

        return bfs
        
        
    def DFS(self, s):
        temp = [s]
        dfs = [s]
        stack = []

        stack, temp = self._key_value(s, stack, temp)

        while stack:
            tempp = stack.pop()
            dfs.append(tempp)

            stack, temp = self._key_value(tempp, stack, temp)

        return dfs
   
   

## 參考資料
# 課堂PPT_BFS：https://docs.google.com/presentation/d/e/2PACX-1vSYJYXUXvGAeTZ5fknxj_-EPm3zxgy4ITdImrXzy63Y-iZgs8uwVNmOaZlnx9fUNzsbo8kphvMTa0c4/pub?start=false&loop=false&delayms=3000&slide=id.p
# 課堂PPT_DFS：https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.p
# 個人github    
