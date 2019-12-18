# Content
 - [if＿name＿ == ＿main＿](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/README.md#if-%EF%BC%BFname%EF%BC%BF--%EF%BC%BFmain%EF%BC%BF)
 - [defaultdict](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/README.md#defaultdict)
 - [Class notes](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/README.md#class-notes)
 - [Depth-First Search](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/README.md#depth-first-search)
 - [BFS vs. DFS](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/README.md#bfs-vs-dfs)
 - [Adjustment of Design DFS](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/README.md#adjustment-of-design-dfs)



# if ＿name＿ == ＿main＿
 > 當主程式時再跑，import時不跑
 
 > 21:20

利用if將class以外的主程式包起來，若此檔案並非成主程式，即不執行

#### Source
[Python - if ＿name＿ == '＿main＿' 涵義](http://blog.castman.net/%E6%95%99%E5%AD%B8/2018/01/27/python-name-main.html)

[Python之父教你寫main()函數](https://codingpy.com/article/guido-shows-how-to-write-main-function/)

[🥧](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/README.md#content)

# defaultdict

#### Source
[python中defaultdict的用法詳解](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/365414/)

[collections雜談之一 ——— dict的key值存不存在乾我屁事](https://ithelp.ithome.com.tw/articles/10193094)

[🍦](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/README.md#content)

# Class notes
- 達克效應（Dunning-Kruger effect）

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/image/1576490058855.jpg)

- John Dewey

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/image/1576490775235.jpg)

[🍧](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/README.md#content)

# Depth-First Search
 > DFS：深度優先搜尋，使用Pre-Order Traversal
 >> 先遇到的就先走訪
 
BFS紀錄會與點數（資料個數）成正比，所以空間個數會較高

從起點開始，逐個走訪每一條路徑，對vertex來說，會先走訪到某一子路徑的最深處，再逐個回溯vertex，繼續走訪尚未走訪的路徑

#### Step
 > 先遇到的就先訪問
 
 從某一vertex出發，不斷地**前進**走訪未曾走訪過的vertex，直到無路可走或所有相鄰的vertex都被走訪過為止，再退回前一個vertex，尋找尚未被走訪的vertex，直到所有相鄰的vertex都被走訪
 
 ![](https://buracagyang.github.io/2019/07/14/breadth-depth-first-search/DFS.gif)

- Step1：先遇到的鄰點就先訪問
  > 可使用stack操作
- Step2：以先遇到的鄰點作為新的搜尋起點
  > pop出來的點，要在push其鄰點（list）進去
- Step3：直到所有「有邊相連的鄰點」都被探索過
  > 全部pop出來後，即為結果

#### Practice
 > by stack
 
 DFS本質上是一種**遞迴（recursion）結構**，其遞迴結構是利用系統的stack達成
  > 當某條路徑走完後，會退回上一個vertex

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/image/1576310235203.jpg)

DFS：使用**stack**紀錄連結到的其他點
 > code：判斷何時要pop、何時要push 
 
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/image/Webp.net-gifmaker1.gif) 
 > Queue中灰色部分，表示當次被提取的值

- 如何判斷值已經處理過：
 將push進stack的值做註記，通常使用染色
  > 若要進入stack判斷：可在stack進行contain
  >> 原始stack不存在此功能

#### Source
[Depth First Search (DFS) Algorithm](https://www.javatpoint.com/depth-first-search-algorithm)

[Graph: Depth-First Search(DFS，深度優先搜尋)](http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)

[Graph DFS Pseudo Code with Animation](https://www.youtube.com/watch?v=GFlthbUd7LQ&feature=youtu.be)

[縱向優先搜尋 (depth-first search)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dfs.html)

[BFS & DFS 學習整理](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/102866/#outline__1_2)

[圖片來源_Step](https://buracagyang.github.io/2019/07/14/breadth-depth-first-search/)

[圖片來源_Practice](http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)

[🍨](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/README.md#content)

# BFS vs. DFS

|  | Design | Time Complexity |  Space Complexity |
| --- | --- | --- | --- |
| **BFS** | Queue | O(V+E) | 與**點數個數**成正比 |
| **DFS** | Stack | O(V+E) | 與**遞迴深度**成正比 |
> 時間複雜度：有多少**鄰邊＆點**
>> V：點的個數\
  E：邊的個數

兩者時間接花在處理queue/stack上，但queue/stack的時間複雜度是相同的

- 差異：需要的記憶體空間
  > 時間複雜度＆記憶體複雜度是相對的
 
  ![](https://i1.kknews.cc/SIG=10hoqj6/ctp-vzntr/s66099p642ns4p8r8o0801o8804p62ps.jpg)
 
    - BFS：把點逐個加入queue，通常需要與**點數**成正比的記憶體空間
      > 一般解決**最短路徑問題**
      >> 暫存多，利用遍歷所有分支的方式，找到最優解
    - DFS：與**遞迴深度**成正比，與點數相比，遞迴深度並不大，所以DFS更加省記憶體空間
      > 一般解決**連通性問題**
      >> 暫存少，從某個分支開始，尋找解（不一定是最優解，但速度較快）
 
 一般來說，較常使用DFS，雖然能使用DFS解決的問題都能用BFS解決，但因為DFS遞迴與耗時小的原因較容易實現
 
 P.S.在最糟的情況下，若DFS選到一條無限長的路徑，stack就會爆掉，這時使用BFS會較佳，因其可以控制queue的長度
 
#### Source
[BFS 和 DFS](https://www.itread01.com/content/1496927052.html)

[深度優先遍歷、廣度優先遍歷(dfs,bfs)詳解](https://kknews.cc/zh-tw/code/3453n3y.html)

[bfs及dfs的比較](https://www.itread01.com/content/1541297601.html)

[DFS && BFS算法学习总结](https://www.jianshu.com/p/8c71c3a2b1a2)


[🍩](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/README.md#content)

# Adjustment of Design DFS
 > 調整作業五DFS程式碼
 
原始DFS程式碼 [👉🏼HERE👈🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/Design%20DFS.py)

在原始程式碼中
 - 使用4個array、1個變數
 - 判斷vertex是否已進入處理（已走訪 or 在stack中待處理）：判斷是否已存在array中
   > 會與array中的值一個個比較，判斷是否已存在
   >> 速度隨著array的大小而變慢
   
 #### Code
 
調整後DFS程式碼 [👉🏽HERE👈🏽](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/Adjustment%20of%20Design%20DFS.py)

- 使用3個array、1個set、1個變數
- 判斷vertex是否已進入處理（已走訪 or 在stack中待處理）：判斷是否已存在set中
  > 會以"字典對應"的方式，判斷是否已存在
  >> 速度不會受到set的大小影響
  
#### Source
[BFS和DFS算法（第2讲）](https://www.youtube.com/watch?v=bD8RT0ub--0&t=)

[🍪](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/README.md#content)
