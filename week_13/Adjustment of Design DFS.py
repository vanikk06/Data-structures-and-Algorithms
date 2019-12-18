# 建立鄰邊表

graph = {} #字典
graph[0] = [1,2]
graph[1] = [2]
graph[2] = [0,3]
graph[3] = [3]

def DFS(s):
    stack = [s]
    dfs = []
    set1 = set()
    
    while stack:
        vertex = stack.pop()
        dfs.append(vertex)
        set1.add(vertex)
        value = graph[vertex]
        for i in value:
            if i not in set1:
                stack.append(i)
        
    return dfs
