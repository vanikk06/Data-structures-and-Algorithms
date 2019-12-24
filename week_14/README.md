# Content

# Disjoint Sets

#### Source
[Disjoint Sets](http://www.csie.ntnu.edu.tw/~u91029/Set.html#5)

[1042 Quiz#1 互斥集合 (Disjoint Sets)](http://squall.cs.ntou.edu.tw/cpp/1042/labtest/test1/DisjointSets.html)

[并查集（Disjoint-set union）第1讲](https://www.youtube.com/watch?v=YKE4Vd1ysPI)

# Minimum Spanning Tree
 > 最小生成樹：關心**邊**的問題
 >> Kruskal's Algorithm
 
 - [Spanning Tree](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#-spanning-tree-)
 - [Practice](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#-practice-)
 - [Exercise](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#-exercise-)
 - [Kruskal's Algorithm](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/README.md#-kruskals-algorithm-)

將複雜問題簡化到graph的問題上，讓graph的edge數字，可以代表某種cost（可將所有可能情形疊加在graph）
 > e.g.花費時間、花費金額...
 
 建立最佳選擇之前，要有一個lower burden（最低負擔）的評估模式

- Minimum Spanning Tree：將複雜問題映射到圖論的問題上，並將最低的花費、成本考量進來
  > 可保留minimum cost，進而規劃後面的資源
  
minimum spanning tree（最小生成樹）有很多實際應用\
將node看作城市，edge看作連線城市的通訊網，edge的weight看作連線城市通訊線路的成本，根據minimum spanning tree建立的通訊網就是這些城市之間成本最低的通訊網


#### § Spanning Tree §

- Spanning Tree：在graph中，可以找到一個tree視為graph的subset
   - 有兩個關鍵，因為是tree：
       1. 不可有loop
       2. 所有node，任兩點一定可以找到path走到對方
          > node不可有isolated（孤立）的情況
          
建立minimum spanning tree有兩個判斷條件：
 > 方式：**邊的個數 = 點-1**
 >> 邊的個數也可作為停止的條件
1. 是否有cycle
2. 是否為連通的tree

#### § Practice §
 > min cost會唯一

edge有weight（權重），其對應的是cost

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/MST_kruskal_en.gif/255px-MST_kruskal_en.gif)

1. 先將cost排序，**由小排到大**，再使用disjoint sets（互斥集、並查集）來作紀錄
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

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/image/MST.gif)


#### § Kruskal's Algorithm §
 > 解決如何生成一個「最小生成樹」的問題
 
需要決定的是「tree產生了沒」，需要在意的是：
1. There is no cycle.
   > disjoint set不斷在看，是否有cycle發生
2. The graph is connected.
   > 兩個方法：
   > 1. 觀察edge是否達到v-1的數量
   > 2. 建tree時，呼叫BFS/DFS走訪
   >> 若連通，即可走完每個點
   

 
 #### Source
 [維基百科_克魯斯克爾演算法](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95)
 
 [Kruskal’s Minimum Spanning Tree Algorithm | Greedy Algo-2](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/)
 
 [[101北一資訊集訓] 06_3_1 MST之Kruskal演算法(NEW)](https://www.youtube.com/watch?v=wuU4DDEUu1w)

[Kruskal's algorithm in 2 minutes — Review and example](https://www.youtube.com/watch?v=71UQH7Pr9kU&feature=emb_logo)

[Check if a given graph is tree or not](https://www.geeksforgeeks.org/check-given-graph-tree/)

[Detect cycle in an undirected graph](https://www.geeksforgeeks.org/detect-cycle-undirected-graph/)
