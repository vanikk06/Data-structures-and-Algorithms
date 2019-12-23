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

將複雜問題簡化到graph的問題上，讓graph的edge數字，可以代表某種cost（可將所有可能情形疊加在graph）
 > e.g.花費時間、花費金額...
 
 建立最佳選擇之前，要有一個lower burden（最低負擔）的評估模式

- Minimum Spanning Tree：將複雜問題映射到圖論的問題上，並將最低的花費、成本考量進來
  > 可保留minimum cost，進而規劃後面的資源
  
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

edge有weight（權重），其對應的是cost

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/MST_kruskal_en.gif/255px-MST_kruskal_en.gif)

先將cost排序，**由小排到大**，再使用disjoint sets（互斥集、並查集）來作紀錄

parent的紀錄先設為 -1
 > 代表尚未走訪過





# 黑板
-1：還沒走訪過
加入edge將-1更改為連結對象，並記錄cost
 > be加入會有loop產生
 
 > 邊滿足即可停止
 
 #### Source
 [維基百科_克魯斯克爾演算法](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95)
 

