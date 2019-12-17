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

使用`defaultdict`套件，來建立vertex鄰邊表

- `__init__`：基本屬性
    - .graph：宣告物件，將參數設定為"list"
        > value的資料型態為list

- `addEdge`：建立「鄰邊」，給定key（u），並在其對應的list新增一個值（v）
    > addEdge(0, 1)：使用**一對**的方式，表示0跟1的edge
    
- `_key_value`：走訪vertex對應的鄰邊，若其已存在於temp或stack/queue中，則不進行處理
      - key：要查詢其鄰邊的vertex
      - method：使用的資料結構
         > queue或stack
      - temp：紀錄已走訪過的vertex
      
     先將key對應到之鄰邊存到value變數中，再對value中的值一個個判斷，他是否已存在於temp中
              - Yes：不處理
              - No：將值新增到method與temp中

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
