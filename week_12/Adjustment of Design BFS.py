# 建立鄰邊表

graph = {} #字典
graph[0] = [1,2]
graph[1] = [2]
graph[2] = [0,3]
graph[3] = [3]

def BFS(s):
    queue = [s]
    bfs = []
    set1 = set()
    
    while queue:
        vertex = queue.pop(0)
        bfs.append(vertex)
        set1.add(vertex)
        value = graph[vertex]
        for i in value:
            if i not in set1:
                queue.append(i)
        
    return bfs
