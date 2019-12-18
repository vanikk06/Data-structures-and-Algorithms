# 建立鄰邊表 

graph = {} #字典
graph[0] = [1,2]
graph[1] = [2]
graph[2] = [0,3]
graph[3] = [3]


def DFS(s):
    temp = [s]
    dfs = [s]
    stack = []
    
    value = graph[s]
    for i in value:
        if not (i in temp):
            stack.append(i)
            temp.append(i)
    
    while stack:
        tempp = stack.pop()
        dfs.append(tempp)
        
        value = graph[tempp]
        for i in value:
            if not (i in temp):
                stack.append(i)
                temp.append(i)
            
    return dfs
