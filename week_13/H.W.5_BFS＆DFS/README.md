# Content
  - []()
  - []()


# Notes

從給定的有向圖，建立此圖該有的資料結構，並以BFS或DFS走訪每個點

- defaultdict：自動建立一個不存在的key，再依照給定參數建立value
  > defaultdict(list)：value自動建立為一個空的list

  >　dictionary：key＆value，value可以是任何值
  
# Code
[🤜🏼HERE🤛🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/H.W.5_BFS%EF%BC%86DFS/H.W.5_BFS_and_DFS.py)

# Demo

- BFS
  > Queue中灰色部分，表示當次提取的值

  ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/image/Webp.net-gifmaker.gif)


- DFS
  > Stack中灰色部分，表示當次提取的值
  
  ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/image/ifmaker1.gif)


# Error

- TypeError
  > `'builtin_function_or_method' object is not subscriptable`
  
  操作錯誤，將pop[0]改為pop(0)即可
