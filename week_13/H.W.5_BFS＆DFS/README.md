# Content
  - [Notes](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_13/H.W.5_BFS%EF%BC%86DFS#notes)
  - [Error](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_13/H.W.5_BFS%EF%BC%86DFS#error)
  - [Code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_13/H.W.5_BFS%EF%BC%86DFS#code)
  - [Demo](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_13/H.W.5_BFS%EF%BC%86DFS#demo)


# Notes

從給定的有向圖，建立此圖該有的資料結構，並以BFS或DFS走訪每個點

- defaultdict：自動建立一個不存在的key，再依照給定參數建立value
  > defaultdict(list)：value自動建立為一個空的list

  > dictionary：key＆value，value可以是任何值


# Error

- TypeError
  > `'builtin_function_or_method' object is not subscriptable`
  
  操作錯誤，將pop[0]改為pop(0)即可


# Code
[🤜🏼HERE🤛🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/H.W.5_BFS%EF%BC%86DFS/H.W.5_BFS_and_DFS.py)

使用`defaultdict`套件，來建立vertex鄰邊表

- `__init__`：基本屬性
    - .graph：宣告物件，將參數設定為"list"
        > value的資料型態為list

- `addEdge`：建立「鄰邊」，給定key（u），並在其對應的list新增一個值（v）
    > addEdge(0, 1)：使用**一對**的方式，表示0跟1的edge
    
- `_key_value`：查看vertex對應的鄰邊，若其已存在於temp中，則不進行處理
     - key：要查詢其鄰邊的vertex
    - method：使用的資料結構，紀錄尚未走訪的鄰邊
       > queue或stack
    - temp：紀錄已走訪過的vertex
      
      先將key對應到之鄰邊存到value變數中，再對value中的值一個個判斷，是否已存在於temp中
      - Yes：不處理
      - No：將值新增到method與temp
     
走訪graph
- `BFS`：廣度優先搜尋，走訪順序根據**與起點距離差異**排序
    > 採Level-Order Traversal，靠近起點的就先走訪
    
    - temp：紀錄已走訪過的vertex
    - bfs：最後結果，按照BFS達到的走訪順序
    - queue：存取vertex的鄰邊，採**先進先出**的資料結構
      
      直接將input放入temp與bfs中，再使用`_key_value`查看input之鄰邊，走訪過或已存放於temp中就不處理，否則即暫存在queue，並紀錄在temp中
    
      使用while迴圈，判斷queue是否為空的：
      
      - No：有尚未走訪的鄰邊存在，要接著走訪
     
        將queue中第一個值取出，將其放入`_key_value`查看其鄰邊，並將其新增在bfs中
        
      - Yes：鄰邊皆已走訪完，回傳最終結果（bfs）
      
- `DFS`：深度優先搜尋，走訪順序根據**遇到的順序**順序
    > 採Pre-Order Traversal，先遇到的就先走訪
    
    - temp：紀錄已走訪過的vertex
    - dfs：最後結果，按照DFS達到的走訪順序
    - stack：存取vertex的鄰邊，採**後進先出**的資料結構
    
      直接將input放入temp與dfs中，再使用`_key_value`查看input之鄰邊，走訪過或已存放於temp中就不處理，否則即暫存在stack，並紀錄在temp中
      
      使用while迴圈，判斷stack是否為空：
      
      - No：有尚未走訪的鄰邊存在，要接著走訪
      
        將stack中最後一個值取出，新增到dfs中，並將其放入`_key_value`查看其鄰邊
         > 必須先進行pop，再丟`_key_value`
         >> 因為stack為先進先出，提取的值為最新加入的（最後一個），若先丟`_key_value`再pop，最後一個值會改變
      
      - Yes：鄰邊皆已走訪完，回傳最終結果（dfs）

# Demo

- BFS
  > Queue中灰色部分，表示當次提取的值

  ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/image/Webp.net-gifmaker.gif)


- DFS
  > Stack中灰色部分，表示當次提取的值
  
  ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/image/ifmaker1.gif)

