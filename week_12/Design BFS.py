# 建立鄰邊表 

graph = {} #字典
graph[0] = [1,2]
graph[1] = [2]
graph[2] = [0,3]
graph[3] = [3]


def BFS(s):
    temp = [s]
    bfs = [s]
    queue = []
    
   
    value = graph[s]
    for i in value:
        if not (i in temp):
            queue.append(i)
            temp.append(i)
    
    while queue:
        value = graph[queue[0]]
        for i in value:
            if not (i in temp):
                queue.append(i)
                temp.append(i)
        
        bfs.append(queue.pop(0))
        
    return bfs
