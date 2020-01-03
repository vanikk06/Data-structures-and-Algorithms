# Content


# Infinite
  > 無限大、無窮
  
#### Source
[]()

# isinstance vs. type


#### Source
[python-isinstance和type的用法和区别](https://www.jianshu.com/p/1f59c4cc3876)

# copy
  > 對list進行複製

複製可區分為「深拷貝」與「淺拷貝」，兩者的差異在於「對新list的變動是否會影響到原本的list」
  > 兩個list在記憶體中是否儲存在同一個區域
  >> `id()`：查詢記憶體位置
  - 深拷貝：兩者完全無關
  - 淺拷貝：在巢狀list，內層仍會有影響

#### code
- 非拷貝方式：使用`=`賦值
   > 以此方式，兩個list是等價的
   ```python
   old = [1, [1, 2, 3], 3]
   new = old
   print('Before:')
   print(old)
   print(new)
   new[0] = 3
   new[1][0] = 3
   print('After:')
   print(old)
   print(new)
   ```
   輸出
   ```python
   Before:
   [1, [1, 2, 3], 3]
   [1, [1, 2, 3], 3]
   After:
   [3, [3, 2, 3], 3]
   [3, [3, 2, 3], 3]
   ```
- 淺拷貝：在內層仍會相互影響
    > 僅拷貝第一層的資料，若第一層的資料中存在list（內層的list），則會因為list內儲存的是記憶體位置，複製會直接複製記憶體位置，因此在內層的list仍會指向相同的記憶體位置
    
    - `copy()`：複製list
        ```python
        old = [1, [1, 2, 3], 3]
        new = old.copy()
        print('Before:')
        print(old)
        print(new)
        new[0] = 3
        new[1][0] = 3
        print('After:')
        print(old)
        print(new)
        ```
        輸出
        ```python
        Before:
        [1, [1, 2, 3], 3]
        [1, [1, 2, 3], 3]
        After:
        [1, [3, 2, 3], 3]
        [3, [3, 2, 3], 3]
        ```
    - 使用解析式列表生成：
        ```python
        old = [1, [1, 2, 3], 3]
        new = [i for i in old]
        print('Before:')
        print(old)
        print(new)
        new[0] = 3
        new[1][0] = 3
        print('After:')
        print(old)
        print(new)
        ```
        輸出
        ```python
        Before:
        [1, [1, 2, 3], 3]
        [1, [1, 2, 3], 3]
        After:
        [1, [3, 2, 3], 3]
        [3, [3, 2, 3], 3]
        ```
    - 使用`for`迴圈遍歷：將元素一個個新增到新的list中
        ```python
        old = [1, [1, 2, 3], 3]
        new = []
        for i in range(len(old)):
            new.append(old[i])
        print('Before:')
        print(old)
        print(new)
        new[0] = 3
        new[1][0] = 3
        print('After:')
        print(old)
        print(new)        
        ```
        輸出
        ```python
        Before:
        [1, [1, 2, 3], 3]
        [1, [1, 2, 3], 3]
        After:
        [1, [3, 2, 3], 3]
        [3, [3, 2, 3], 3]
        ```
    - 使用`[:]`切片：
         ```python
         old = [1, [1, 2, 3], 3]
         new = old[:]
         print('Before:')
         print(old)
         print(new)
         new[0] = 3
         new[1][0] = 3
         print('After:')
         print(old)
         print(new)
         ```
         輸出
         ```python
         Before:
         [1, [1, 2, 3], 3]
         [1, [1, 2, 3], 3]
         After:
         [1, [3, 2, 3], 3]
         [3, [3, 2, 3], 3]
         ```
- 深拷貝：兩者相互獨立
    - `copy.deepcopy()`：不論多少層，得到的list對原來的list都不影響
      > 要匯入`copy`套件
        ```python
        import copy
        
        old = [1, [1, 2, 3], 3]
        new = copy.deepcopy(old)
        print('Before:')
        print(old)
        print(new)
        new[0] = 3
        new[1][0] = 3
        print('After:')
        print(old)
        print(new)
        ```
        輸出
        ```python
        Before:
        [1, [1, 2, 3], 3]
        [1, [1, 2, 3], 3]
        After:
        [1, [1, 2, 3], 3]
        [3, [3, 2, 3], 3]
        ```
    

#### Source
[深入淺析Python中list的複製及深拷貝與淺拷貝](https://www.itread01.com/article/1535941191.html)

# Adjacency Matrix
  > 鄰接矩陣

# Class notes

- 演算法：生活應用問題的延伸，觀摩演算法的想法可以引起對生活議題的不同看法，重新解構問題，抽象化並一步步歸納解決方法

# Shortest Path
  > 最短路徑：關心**邊**的問題
  >> 此為Dijkstra's Algorithm

常用在路徑規劃中，最小距離的估算方式

計算graph上從起點到終點哪裡有**最短路徑（cost最低）**
  > e.g.Google map的參考路徑：以時間為標的、以費用為標的（是否上高速公路）...
  >> 若將cost轉為價格，尋找價格最低的路徑，時間會拉長\
  >> 若將cost轉為時間，尋找時間最少的路徑，價格會拉高
  
#### § Practice §


起點固定，紀錄走到vertex的cost，若走不到則記錄∞（無限大），再慢慢增加最小cost的vertex，增加的vertex與起點可以共同被取用（可用可不用）
  > 當graph複雜，查看會很困難，使用edge表（包含weight、起點、終點）較優
  
 ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_15/image/output_HGOiV3.gif)

- 若cost大小相同，可自行制定取用順序
  > 相同cost先後沒差，最後結果都會收斂
- 可被取用的vertex，其cost已為最小cost，記錄重複抄寫即可
  > 不須updata
- 新增的vertex重新計算cost的對象，只要考慮新增vertex產生的所有可能path即可，再選出最小的cost
  > 調整過的cost可自行作下標紀錄

#### § Exercise §
- 加入edge表格
  > 小心，edge為無向，只要連結都要考慮
  
  ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_15/image/output_8P7AbS.gif)
  
#### § Time Complexity §
   > O(V²)

分成兩部份：
  1. 加入vertex、edge：每個vertex只加入一次，每個edge也只加入一次，時間複雜度會剛好是走訪整個graph的時間
    > O(V+E)
    
  2. 尋找下一個vertex：從長度為V的list中，尋找當中cost的最小值，所以為O(V)；總共有V個點，所以全部總共為O(V²)
  
整體來說，時間複雜度為O(V²)
 
#### Source
[Dijkstra’s shortest path algorithm | Greedy Algo-7](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)

[Question: Link State Routing Algorithm With Dijkstra's Algorithm. Please Provide The Forwarding Table And Explain How It Was Obtained](https://www.chegg.com/homework-help/questions-and-answers/link-state-routing-algorithm-dijkstra-s-algorithm-please-provide-forwarding-table-explain--q26034913)

[Dijkstra Algorithm Example](https://www.youtube.com/watch?v=0nVYi3o161A&feature=emb_logo)

[Single Source Shortest Paths:
Dijkstra's Algorithm](http://www.csie.ntnu.edu.tw/~u91029/Path.html#4)
