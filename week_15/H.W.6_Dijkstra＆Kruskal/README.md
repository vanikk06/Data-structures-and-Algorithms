# Content

# Notes

- graph：有起點、終點、cost
- `addEdge`：新增edge，加上權重
    > idea：使用dict紀錄
    - u：起點
    - v：終點
    - w：權重
- 測資皆為正整數

Dijkstra先建一個權重的matrix（index由由0開始，為nxn矩陣）
  > 回傳值：input到每vertex的最短距離
  >> type dictionary

Kruskal建立edge不侷限用defaultdict
   > 回傳值：從最小的weight開始，起點-終點（小-大）

# Error

- TyprError
   > `unsupported operand type(s) for +: 'int' and 'str'`
   >> 類型錯誤：不支持操作類型為整數和字串
   
    `+`：符號操作，可分兩類
    - 數學運算符：在int、float等數字類型資料之間進行加法的操作
    - 字串連接：對str的資料類型進行連接的動作
    
    在`+`出現在**既有數字類型資料又有字串類型資料**的情況下，python會不知道是要進行數字運算還是字串連接的動作

#### Source
[Python初學者錯誤：TypeError: unsupported operand type(s) for +: 'int' and 'str'](https://blog.csdn.net/foryouslgme/article/details/51536882)


 - ⭐assignment⭐
    > 指派、賦值
   
   在python中`=`代表的是一個指派、賦值的動作，讓變數在記憶體中定址\
   當執行兩個變數相互指派的程式碼時，代表的是讓**兩個變數定址在相同的記憶體位置**
   ```python 
   a = [3]
   b = []
   
   b = a
   b.append(7)
   
   print('a = ', a)
   print('b = ', b)
   print( a is b )
   ```
   因為是在相同的記憶體位置，因此對其中一個變數作出變動時，會直接影響到另一個變數
   ```python
   a =  [3, 7]
   b =  [3, 7]
   True
   ```
   如果想要將a變數的值儲存到b變數內，但不想讓對b變動的變動影響到a變數的話，可以使用`.copy()`函式
    ```python 
   a = [3]
   c = []
   
   c = a.copy()
   c.append(8)
   
   print('a = ', a)
   print('c = ', c)
   print( a is c )
   ```
   結果
   ```python
   a =  [3, 7]
   c =  [3, 7, 8]
   False
   ```

# Code

使用`collections.defaultdict`套件

- `__init__`：基本屬性
    - .V：vertex個數
    - .graph：Dijkstra使用之adjacency matrix
    - .graph1：Kruskal使用之字典，資料類型為`defaultdict`，參數為int
    - .graph_matrix：Dijkstra使用之紀錄cost的矩陣

- `addEdge`：建立edge，有三個參數
    - u：src，起點
    - v：dest，終點
    - w：weight/cost，權重、成本
- `Dijkstra`：最短路徑
    > 有一個參數：起點
    
    
    


