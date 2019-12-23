# 黑板
-1：還沒走訪過
加入edge將-1更改為連結對象，並記錄cost
 > be加入會有loop產生
 
 > 邊滿足即可停止


# Minimum Spanning Tree
 > 最小生成樹：關心**邊**的問題
 >> Kruskal's Algorithm

將複雜問題簡化到graph的問題上，讓graph的edge數字，可以代表某種cost（可將所有可能情形疊加在graph）
 > e.g.花費時間、花費金額...
 
 建立最佳選擇之前，要有一個lower burden（最低負擔）的評估模式

- Minimum Spanning Tree：將複雜問題映射到圖論的問題上，並將最低的花費、成本考量進來
  > 可保留minimum cost，進而規劃後面的資源
  
#### Spanning Tree

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
