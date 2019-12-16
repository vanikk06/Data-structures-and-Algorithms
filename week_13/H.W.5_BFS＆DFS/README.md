給圖，建此圖該有的資料結構，並以BFS或DFS走訪每個點

- defaultdict：自動建立一個不存在的key，再依照給定參數建立value
  > defaultdict(list)：value自動建立為一個空的list

  >　dictionary：key＆value，value可以是任何值
  
- graph：本身為list

# Error

- TypeError
  > 'builtin_function_or_method' object is not subscriptable
  
 操作錯誤，將pop[0]改為pop(0)即可
