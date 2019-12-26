# Content
 - [Greedy Algorithm](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#greedy-algorithm)
 - [sort vs. sorted](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#sort-vs-sorted)
 - [Disjoint Sets](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#disjoint-sets)
 - [Minimum Spanning Tree](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#minimum-spanning-tree)

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

[👪](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#content)

# sort vs. sorted
 > 排序對象要屬於相同資料型態

- `list.sort(key=None, reverse=False)`
  > 此函式會直接變動到原始的資料內容
 
- `sorted(list, key=None, reverse=False)`
  > 此函示不會變動到原始的資料內容
  >> 要使用變數來儲存回傳值

不設定任何條件的話，字串會按照字母排序排列、數字則會遞增排列
  > 相反：`reverse=True`

#### Source
[Python 初學第十講 — 排序](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-f3148ebb33a4)

[Python 初學第六講 — 串列的更多操作](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-f1b4e7d2e5ac)

[python sort()和sorted()區別](https://kknews.cc/zh-tw/code/p6mo3xp.html)

[👨‍👩‍👦](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#content)

# Disjoint Sets
 > 互斥集合、併查集\
 又稱為union-find資料結構、merge-find資料結構
 >> 資料結構：檢查一個graph是否存在一個cycle
 
 一堆集合中，各自擁有的元素都各不相同，也就是集合與集合之間彼此沒有交集
 
- union-find：給出n個vertex，vertex與vertex之間要麼連通要麼不連通，此為實現連通函數（union）以及判斷vertex之間是否為直接連通或間接連通（connected）的函數
  > disjoint sets的合併及查詢
 
功能：
 > 皆為O(log n)，平均為O(α(n))
 >> 其中α(n)是Ackermann function f(N,N) 的反函數
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

[👨‍👩‍👧](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#content)

# Minimum Spanning Tree
 > 最小生成樹：關心**邊**的問題
 >> Kruskal's Algorithm：採Greedy Algorithm
 
 - [Spanning Tree](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#-spanning-tree-)
 - [Practice](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#-practice-)
 - [Exercise](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#-exercise-)
 - [Kruskal's Algorithm](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#-kruskals-algorithm-)
 - [Time Complexity](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#-time-complexity-)

將複雜問題簡化到graph的問題上，讓graph的edge數字，可以代表某種cost（可將所有可能情形疊加在graph）
 > e.g.花費時間、花費金額...
 
 建立最佳選擇之前，要有一個lower burden（最低負擔）的評估模式

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
 
需要決定的是「tree產生了沒」，需要在意的是：
1. There is no cycle.
   > disjoint set不斷在看，是否有cycle發生
2. The graph is connected.
   > 兩個方法：
   > 1. 觀察edge是否達到v-1的數量
   > 2. 建tree時，呼叫BFS/DFS走訪（若連通，即可走完每個點）
   
#### § Time Complexity §

排序graph上所有的edge，為O(E log E)
 > 與heap sort樹狀排序相同
 

 
 #### Source
 [維基百科_克魯斯克爾演算法](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95)
 
 [Kruskal’s Minimum Spanning Tree Algorithm | Greedy Algo-2](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/)
 
 [[101北一資訊集訓] 06_3_1 MST之Kruskal演算法(NEW)](https://www.youtube.com/watch?v=wuU4DDEUu1w)

[Kruskal's algorithm in 2 minutes — Review and example](https://www.youtube.com/watch?v=71UQH7Pr9kU&feature=emb_logo)

[Check if a given graph is tree or not](https://www.geeksforgeeks.org/check-given-graph-tree/)

[Detect cycle in an undirected graph](https://www.geeksforgeeks.org/detect-cycle-undirected-graph/)

[Spanning Tree](http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html)

[👨‍👩‍👧‍👦](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#content)
