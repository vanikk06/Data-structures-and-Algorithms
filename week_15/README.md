# H.W.6_Dijkstra＆Kruskal
[🤜🏻HERE🤛🏻](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15/H.W.6_Dijkstra%EF%BC%86Kruskal)
  
- [Jupyter notebook_The process of learning Kruskal & Dijkstra](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_15/H.W.6_Dijkstra%EF%BC%86Kruskal/The%20process%20of%20learning%20Kruskal%20%26%20Dijkstra.ipynb)
  - [Jupyter nbviewer_The process of learning Kruskal & Dijkstra](https://nbviewer.jupyter.org/github/vanikk06/Data-structures-and-Algorithms/blob/master/week_15/H.W.6_Dijkstra%EF%BC%86Kruskal/The%20process%20of%20learning%20Kruskal%20%26%20Dijkstra.ipynb)
- [Notes](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15/H.W.6_Dijkstra%EF%BC%86Kruskal#notes)
- [Error](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15/H.W.6_Dijkstra%EF%BC%86Kruskal#error)
- [Code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15/H.W.6_Dijkstra%EF%BC%86Kruskal#code)
- [Demo](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_15/H.W.6_Dijkstra%EF%BC%86Kruskal#demo)
- [Other student works](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15/H.W.6_Dijkstra%EF%BC%86Kruskal#other-student-works)
    - [Dijkstra](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15/H.W.6_Dijkstra%EF%BC%86Kruskal#dijkstra-1)
    - [Kruskal](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15/H.W.6_Dijkstra%EF%BC%86Kruskal#kruskal-1)


# Content
  - [String Type](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#string-type)
  - [Infinite](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#infinite)
  - [isinstance vs. type](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#isinstance-vs-type)
  - [copy](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#copy)
  - [Adjacency Matrix](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#adjacency-matrix)
  - [Class notes](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#class-notes)
  - [Shortest Path](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#shortest-path)
  
  
  
# String Type
  > 字串型態
  >> python致力簡潔易讀
  
在python中，基本的字串表示方式是以`''`、`""`表示

```python
'hey'"4"

#輸出
'hey4'
```
> 若有兩個連續字串，python會自動將它們結合為一個字串

- 跳脫字元：`\`
  > 在字串中若包含`\`會將此認定為自動轉換為`\\`

```python
'c:\workspace'

#輸出
'c:\\workspace'
```
會等價於
```python
'c:\\workspace'

#輸出
'c:\\workspace'
```
想要表示原始字串（Raw String），可在字串前加上`r`

若自字串前加入，會將所有`\`接轉換為`\\`\
若搭配`print()`函式，`\\`會顯示為`\`
```python
r'c:\workspace'
#輸出
'c:\\workspace'


r'c:\\workspace'
#輸出
'c:\\\\workspace'

print('c:\workspace')
#輸出
c:\workspace


print(r'c:\workspace')
#輸出
 c:\workspace


print('c:\\workspace')
#輸出
 c:\workspace

print(r'c:\\workspace')
#輸出
 c:\\workspace
```

#### Others

其他常用的跳脫字串表示
- `\\`：反斜線
- `\'`：單引號
- `\"`：雙引號
- `\n`：換行
- `\t`：Tab
- `\r`：歸位

```python
'I'm tall'
#輸出
SyntaxError: invalid syntax


'I\'m tall'
#輸出
"I'm tall"


r'I\'m tall'
#輸出
"I\\'m tall"
```

```python
print('v\na')
#輸出
v
a


print(r'v\na')
#輸出
v\na
```

#### Source
[字串型態](https://openhome.cc/Gossip/Python/StringType.html)

[🌊](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#content)

# Infinite
  > 無限大、無窮大
  
在python表示無限大：
  > 通過`float()`創建
  - `float('inf')`：正無限大
  - `float('-inf')`：負無限大

此無限大與數學運算邏輯相同
1. 與任意常數運算：皆為無限大
   > 比較中，比任何數都大
   >> 正無限大 ＞ 負無限大
2. 放置於分母：0.0
   > 在此無限大以符點數表示

可使用`math.isinf()`進行判斷
```python
import math

a = float("inf")    #正無限大
b = float("-inf")   #負無限大

math.isinf(a)       #True
math.isinf(b)       #True
```

若將正無限大與負無限大共同運算，會得到`NaN`
  - `nan`：not a number
     > 對`nan`進行操作，不會出現error
 
任何數與`nan`進行比較，皆返回False

可使用`math.isnan()`進行判斷
```python
import math

c = float('nan')

math.isnan(c)                 #True

#比較
float("nan") == float("nan")  #False
float("inf") == float("inf")  #True

c > 3                         #False
```
 



#### Source
[python中的無窮大](https://segmentfault.com/a/1190000011908915)

[💧](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#content)

# isinstance vs. type
  > instance：實例，用class建造出來的物件
  >> instantiation：實例化

在python中，通常使用`isinstance()`和`type()`這兩個內建函式來判斷**變數屬於何種資料類型（class）**

最大差異：判斷對象是否已知

- `isinstance()`：判斷物件是否是某個class或child class的實例
   > isinstance(object, type-or-tuple-or-class)
   >> 回傳值：bool
   
   - object：要判斷的物件
   - type-or-tuple-or-class：要判斷的類型，可以是一個或多個
     > 多個：tuple，符合其中任意一個元素，及回傳True
   
   
   判斷為何種資料類型
   ```python
   a = 5
   
   isinstance (a, int)            #True
   isinstance (a, str)            #False
   
   isinstance (a, (str,int,list))   #True
   isinstance (a, (str,list,float)) #False
   ```
   判斷是否為class之實例
   ```python
   class A(object):    #創建class
    pass
   
   a=A()
   isinstance(a,A)     #True
   ```

- `type`：得到物件的資料類型（class）
   > type(object)
   
   
   ```python
   class A(object):    #創建class
    pass
   
   a=A()
   type(a)             #__main__.A
   type(a) == A        #True
   ```
   
#### 總結

- 共同點：皆可判斷物件屬於何種類型

- 相異點：
    1. 判斷方式
        - `isinstance()`：兩個參數
           > 像是問「物件和xxx是相同類型嗎？」
           >> 只能判斷**已知**，一定要有個判斷的類型對象
        - `type()`：一個參數
           > 像是問「物件是什麼類型的？」
           >> 能夠判斷**未知**
    2. class存在繼承關係時
        - `isinstance()`：主要功能
        - `type()`：不適合，此判斷的物件是物件為主class（`__main__.class名`）
        
       ```python
       class father(object):
            pass

       class son(father):
            pass

       a = father()
       b = son()

       isinstance(b ,father)     #True

       type(b)                   #__main__.son
       type(b) == father         #False
       ```
       `type(b)`判斷出的類型為`__main__.son`，所以拿`type(b)`去與`son()`的parent class`father()`判斷，自然會是不匹配的


#### Source
[python-isinstance和type的用法和区别](https://www.jianshu.com/p/1f59c4cc3876)

[🔥](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#content)

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

[❄](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#content)

# Adjacency Matrix
  > 鄰接矩陣、伴隨矩陣
  >> 紀錄vertex彼此的關聯

adjacency matrix是一種graph結構中常用的表示方法\
用**數字方陣**紀錄各個vertex之間「是否有edge相連」，數字大小可以表示edge的weight大小或edge個數
  
- 方陣：A<sub>nxn</sub>，n為graph中vertex個數
  > A(vertex, vertex)
  >> e.g. A(0, 2)：vertex 0與vertex 2
  
  | | (0) | (1) | (2) | (3) |
  | --- | --- | --- | --- | --- |
  | **(0)** | 0 | 4 | 0 | 1 |
  | **(1)** | 4 | 0 | 9 | 1 |
  | **(2)** | 0 | 9 | 0 | 0 |
  | **(3)** | 1 | 1 | 0 | 0 |
  - 方陣內儲存連結資訊，可以是任何任意兩點之間的資訊
    > 但僅能記錄一筆資料
      
可以透過adjacency matrix還原graph

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_15/image/Snipaste_2020-01-06_01-16-37.png)

#### Source
[維基百科_鄰接矩陣](https://zh.wikipedia.org/wiki/%E9%82%BB%E6%8E%A5%E7%9F%A9%E9%98%B5)

[Graph 資料結構 :Adjacency Matrix](http://www.csie.ntnu.edu.tw/~u91029/Graph.html#3)

[☃](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#content)

# Class notes

- 演算法：生活應用問題的延伸，觀摩演算法的想法可以引起對生活議題的不同看法，重新解構問題，抽象化並一步步歸納解決方法

[⛄](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#content)

# Shortest Path
  > 最短路徑：關心**邊**的問題
  >> 此為Dijkstra's Algorithm

常用在路徑規劃中，最小距離的估算方式

  - [Practice](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#-practice-)
  - [Exercise](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#-exercise-)
  - [Time Complexity](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#-time-complexity-)


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
- 關鍵
  1. 可被採用的vertex，其cost必然已是min cost
  2. 新增的vertex，只會影響與其相連接的vertex
  
- 加入edge表格
  > 小心，edge為無向，只要連結都要考慮
  
  ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_15/image/output_8P7AbS.gif)
  

- 有向線與無向線混合
  
  ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_15/image/output_cJiS8V.gif)
  
- 僅有向線

  ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_15/image/output_L3488F.gif)

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

[⚡](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_15#content)
