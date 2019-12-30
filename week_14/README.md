# Content
 - [sort vs. sorted](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#sort-vs-sorted)
 - [Greedy Algorithm](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#greedy-algorithm)
 - [Disjoint Sets](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#disjoint-sets)
 - [Minimum Spanning Tree](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#minimum-spanning-tree)


# key vs. value

#### Source
[Python基礎——字典中由value查key的幾點說明](https://blog.csdn.net/ywx1832990/article/details/79145576)

[👨‍👩‍👦‍👦](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)


# sort vs. sorted
 > 排序對象要屬於相同資料型態

- `list.sort(reverse=False, key=None)`
  > list內建的排序方法（限用list）
  >> 此函式會直接變動到原始的資料內容
 
- `sorted(list,  reverse=False, key=None)`
  > python內建**全域性**的排序方法（對所有可迭代序列皆有效）
  >> 此函示不會變動到原始的資料內容\
  要使用變數來儲存回傳值

不設定任何條件的話，字串會按照字母排序排列、數字則會遞增排列
  > 相反：`reverse=True`
  
#### dict sorted

- [以key排序](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#%E4%BB%A5key%E6%8E%92%E5%BA%8F)
- [以value排序](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#%E4%BB%A5value%E6%8E%92%E5%BA%8F)

##### 以key排序
dict內元素本身為無序，若想依照某個特定的順序來取用dict內的元素，則需要使用`for`迴圈 + `sorted()`對其進行排序

- 舉例，直接對dict執行`sorted()`
   ```python
   d = {}
   d[4] = 'four'
   d[1] = 'one'
   d[2] = 'two'
   d[5] = 'five'
   d[3] = 'three'
   d
   ```
   回傳：
   ```python
   {4: 'four', 1: 'one', 2: 'two', 5: 'five', 3: 'three'}
   ```
   使用`sorted()`排序
   ```python
   test = sorted(d)
   print(test)
   print(type(test))
   ```
   回傳：
   ```python
   [1, 2, 3, 4, 5]
   <class 'list'>
   ```
直接進行`sorted()`，只會對dict的所有`key`值作排序，而非將`key`與`value`一同排序\
因此需要搭配`for`迴圈，依照已排序好的`key`值找其對應到的`value`

   ```python
   sorted_d = dict()

   for i in sorted(d):
       sorted_d[i] = d[i]

   sorted_d
   ```
   回傳：
   ```python
   {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
   ```

##### 以value排序

使用key參數來指定排序之前要跳用的函式\
在`sorted()`函式的key參數稱為`key function`，可以自行指定排序依據的函數，當`sorted()`與`key function`搭配使用，`sorted()`會將所有要排序標的中的元素一個個丟進`key function`中，得到和標的元素一樣多的回傳值，再根據這些回傳值對原始的標的進行排序
> 因為是根據`key function`的回傳值進行排序，因此`function`的參數只能是list當中的**元素**，而不是整個list

```python
sorted(d.items(), key=lambda d: d[1])
```
 - `items()`：存取dict當中所有的`key-value`元素
   > 回傳值為一個list，其元素皆為tuple形式的`(key, value)`
   
在此`key function`使用的是一個十分特別的function，叫作`lambda function`
 - `lambda function`：簡化的function定義方式
      - 在`lambda`後面的值：是這個function的參數
         > 在此為`d`
      - `:`後面的值：這個function的回傳值
         > 在此為`d[1]`
         >> 意思為，當這個`key function`每次拿到一個tuple作為參數，就取出index為1的值回傳

- 範例，建立dict
   ```python
   d = {}
   d['45'] = 4
   d['1'] = 1
   d['52'] = 2
   d['76'] = 5
   d['30'] = 3
   d
   ```
   回傳
   ```python
   {'45': 4, '1': 1, '52': 2, '76': 5, '30': 3}
   ```
   搭配`lambda function`對`value`進行排序
    > `sorted()`的回傳值為list，再搭配`for`迴圈的方式將其轉回dict
   ```python
   test = sorted(d.items(), key=lambda d:d[1])
   
   temp = {}
   for i in range(len(test)):
        temp[test[i][0]] = test[i][1]

   temp
   ```
   回傳
   ```python
   {'1': 1, '52': 2, '30': 3, '45': 4, '76': 5}
   ```

#### Source
[Python 初學第十講 — 排序](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-f3148ebb33a4)

[Python 初學第六講 — 串列的更多操作](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-f1b4e7d2e5ac)

[python sort、sorted高階排序技巧](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/373191/)

[排序指南](https://docs.python.org/zh-cn/3/howto/sorting.html)

[👨‍👩‍👦](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)

# Greedy Algorithm
 > 貪婪演算法、貪心演算法
 >> 尋找「最佳解」的方法
 
 尋找方法：在每一步選擇中都採取**當前看起來最好的選擇**，進而希望最終答案是**最佳的**方法
  > 不斷的改進解答，直到無法改進為止
  
 使用此演算法的前提是，必須確保局部最佳解能解決全域最佳解
  > 簡單的說，問題能夠分解為子問題來解決，子問題的最佳解能遞推到最終問題的最佳解
  
 可以解決一些最佳化問題，但一般無法得到理想中的答案（沒有測試所有可能的解，容易**過早做決定**，因而無法達到最佳解）
  > 可解決e.g. Minimal Spanning Tree、Huffman Coding（哈夫曼編碼）...
  >> 一個問題如果可以通過greedy algorithm來解決，那通常greedy algorithm是解決此問題的最好辦法
 

#### Source
[貪婪演算法](https://zh.wikipedia.org/wiki/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95)

[貪婪演算法(Greedy)](https://www.csie.ntu.edu.tw/~b98902112/cpp_and_algo/cpp02/greedy.html)

[貪婪式演算法的原理](http://ccckmit.wikidot.com/so:greedyalgorithm)

[👪](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)


# Disjoint Sets
 > 互斥集合、併查集\
 又稱為union-find資料結構、merge-find資料結構
 >> 資料結構：檢查一個graph是否存在一個cycle
 
 一堆集合中，各自擁有的元素都各不相同，也就是集合與集合之間彼此沒有交集
 
- union-find：給出n個vertex，vertex與vertex之間要麼連通要麼不連通，此為實現連通函數（union）以及判斷vertex之間是否為直接連通或間接連通（connected）的函數
  > disjoint sets的合併及查詢
 
功能：
 - union：將兩個set做聯集，合併成一個set
 - find：尋找一個元素是在哪個set
 - split：將一個set拆成兩個set
 
#### 操作
將edge連接的vertex放到同一個set裡面，若連接的vertex已存在別的set中，則將兩個set合併
 > 同一個set：站在任一個vertex上，都可以走到相同set的任意一個vertex
 >> 若選中的edge其連接的vertex已存在同一個set中，即會出現cycle

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/image/Snipaste_2019-12-24_16-22-02.png)

使用一個array，紀錄每個vertex的parent\
每個vertex先預設為-1
> -1：獨立的vertex

在同一個set中，找一個vertex A作為parent，並將相同set的其他vertex其parent更改為A\
當合併兩個set時，將其parent改為相同即可\
當edge連接的vertex已有相同的parent時，代表採用此edge即會出現cycle

#### Source
[Disjoint Sets](http://www.csie.ntnu.edu.tw/~u91029/Set.html#5)

[1042 Quiz#1 互斥集合 (Disjoint Sets)](http://squall.cs.ntou.edu.tw/cpp/1042/labtest/test1/DisjointSets.html)

[并查集（Disjoint-set union）第1讲](https://www.youtube.com/watch?v=YKE4Vd1ysPI)

[普林斯頓課程學習筆記1 Union-find](https://medium.com/@gxyou45/algorithm%E6%99%AE%E6%9E%97%E6%96%AF%E9%A0%93%E8%AA%B2%E7%A8%8B%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%981-union-find-5af7911ca5ef)

[👨‍👩‍👧](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)

# Minimum Spanning Tree
 > 最小生成樹：關心**邊**的問題
 >> 此為Kruskal's Algorithm：採Greedy Algorithm
 
 - [Spanning Tree](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#-spanning-tree-)
 - [Practice](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#-practice-)
 - [Exercise](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#-exercise-)
 - [Kruskal's Algorithm](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#-kruskals-algorithm-)
 - [Time Complexity](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#-time-complexity-)

將複雜問題簡化到graph的問題上，讓graph的edge數字，可以代表某種cost（可將所有可能情形疊加在graph）
 > e.g.花費時間、花費金額...
 
 建立最佳選擇之前，要有一個lower burden（最低負擔）的評估模式\
 以最小的cost走訪完每個vertex

- Minimum Spanning Tree：將複雜問題映射到圖論的問題上，並將最低的花費、成本考量進來
  > 可保留minimum cost，進而規劃後面的資源
  
minimum spanning tree（最小生成樹）有很多實際應用\
將node看作城市，edge看作連線城市的通訊網，edge的weight看作連線城市通訊線路的成本，根據minimum spanning tree建立的通訊網就是這些城市之間成本最低的通訊網



#### § Spanning Tree §

- Spanning Tree：在graph中，可以找到一個tree視為graph的subset（此tree包含graph的所有vertex）
   - 有兩個關鍵，因為是tree：
       1. 不可有loop
       2. 所有node，任兩點一定可以找到path走到對方（完全連通）
          > node不可有isolated（孤立）的情況
          >> 若graph並非完全連通，則沒有spanning tree，而是擁有許多棵spanning sub-tree（生成子樹）構成的spanning forest（生成森林）
          
建立minimum spanning tree有兩個判斷條件：
 > 方式：**邊的個數 = 點-1**
 >> 邊的個數也可作為停止的條件
1. 是否有cycle
2. 是否為連通的tree

可以想像成許多的MST做作union（聯集）
 > 用disjoint set作為union-find之輔助
1. root不同即可union
2. root相同不可union
   > 會出現cycle

#### § Practice §
 > min cost會唯一

edge有weight（權重），其對應的是cost

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/MST_kruskal_en.gif/255px-MST_kruskal_en.gif)

1. 先將cost排序，**由小排到大**，從小的開始，再使用disjoint sets（互斥集、併查集）來作紀錄
2. parent的紀錄先設為 -1，當有edge加入時，再將-1更改為起點，並記錄cost
   > -1：代表尚未走訪過 
3. 按照sorted順序慢慢加入，方向性先固定，左邊是起點右邊是終點，當邊數滿足即可停止
   > 假設左邊為右邊的root
   >> 會產生loop的edge就不放入
4. 最後吐出graph min cost的路徑與minimum cost

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/image/Snipaste_2019-12-24_16-22-02.png)
 > 此為記錄parent，edge增加parent就可能要update
 >> 紀錄可採linked list的方式（如圖），方便查詢即可
 
☆ 將兩個disjoint set合併時，要決定誰要當root
  > 先確定一個方向（src當parent還是dest當parent），置換或合併時採相同的動作


#### § Exercise §
 > 儲存紀錄對象：edge

- 畫圖表示，無使用edge表紀錄採用的edge與其cost

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/image/MST.gif)


- 畫圖表示，並且使用edge表紀錄採用的edge與其cost

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/image/output_UjbChm.gif)


#### § Kruskal's Algorithm §
 > 解決如何生成一個「最小生成樹」的問題
 >> 是處理minimum spanning tree最經典的一個作法
 
需要決定的是「tree產生了沒」，需要在意的是：
1. There is no cycle.
   > disjoint set不斷在看，是否有cycle發生
2. The graph is connected.
   > 兩個方法：
   > 1. 觀察edge是否達到v-1的數量
   > 2. 建tree時，呼叫BFS/DFS走訪（若連通，即可走完每個點）
   
#### § Time Complexity §
 > O(E log E)或O(E log V)

- 前面的E：要先排序edge，所以會先走訪完全部的邊

- 後面的E/V： E = V-1（1過小可忽略），所以E = V
- log：每走訪一個E/V次數是隨log指數減少的
 
 #### Source
 [維基百科_克魯斯克爾演算法](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95)
 
 [Kruskal’s Minimum Spanning Tree Algorithm | Greedy Algo-2](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/)
 
 [[101北一資訊集訓] 06_3_1 MST之Kruskal演算法(NEW)](https://www.youtube.com/watch?v=wuU4DDEUu1w)

[Kruskal's algorithm in 2 minutes — Review and example](https://www.youtube.com/watch?v=71UQH7Pr9kU&feature=emb_logo)

[Check if a given graph is tree or not](https://www.geeksforgeeks.org/check-given-graph-tree/)

[Detect cycle in an undirected graph](https://www.geeksforgeeks.org/detect-cycle-undirected-graph/)

[Spanning Tree](http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html)

[👨‍👩‍👧‍👦](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)
