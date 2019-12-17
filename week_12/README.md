# Content
- [Level-Order Traversal](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_12#level-order-traversal)
- [Graph](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_12#graph)
- [Breadth-First Search](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_12#breadth-first-search)

# Dict & Set
 > 字典（dictionary）與集合
 
- [Dict]()
- [Set]()

## Dict
 > 字典：關聯式陣列 or hash table
 >> {'key'：'value'}
 
- `.update(x)`：合併 
- `.keys()`：取所有鍵（key）
- `.values()`：取所有值（value）
- `.items()`：取所有鍵值對（key, value）

## Set
 > 集合：建立一個無序、不重複的元素集
 >> 想像成僅留下key的dict

與tuple、list類似，不同的是set**不會包含重複的值**

- 宣告＆建立集合
  - `set1 = set()`：建立空的集合
    > ☆建立空集合的方法是`set1 = set()`而非`set1 = {}`
    >> {}表示空的dict
  - `set2 = {1, 2, 3, 4}`
- 基本操作
  - `.add()`：新增元素
  - `.remove()`：




#### Source
[]()

[]()


[🖌](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_12#content)

# Level-Order Traversal

各個node相對於root有其對應的level，按照**level由小到大**的順序對node進行走訪

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_12/image/1576400035124.jpg)

#### Source
[Binary Tree: Traversal(尋訪) - Level-Order Traversal](http://alrightchiu.github.io/SecondRound/binary-tree-traversalxun-fang.html#level)

[✏](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_12#content)

# Graph
  > 圖：由**點＆線**組成
  
- 定義  
  graph比tree更加廣義，不限制結構裡的node/vertex只能有唯一的parent
    > 優點：能以**關係**表示先後
    
  graph為所有的vertex/node與edge所組成之集合
    - vertex/node：資料節點 
    - edge：線段、連結
      > 實際上，是用一對vertex表示edge
      >> e.g.(v1, v2)：即為連結v1與v2的edge
    

      根據edge是否具有**方向性**
      - directed graph：edge具有方向性，及vertexA與vertexB之關係為**單向的**
        > 有向圖
      - undirected graph：edge不具有方向性，及vertexA與vertexB之關係為**雙向的**
        > 無向圖

- graph vs. tree

    與tree不同，可以有loop（迴路）
      > loop：可以繞回原點（root）

  - tree是graph的子集合
    - graph：由**點**跟**線**組成，即為graph
    - 在graph中砍掉loop的線，並且點有上跟下的關係，即為tree
      > tree被蘊含在graph中

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_12/image/1576310235203.jpg)

紀錄graph方式：使用array＆linked list
  - array：點
    >　長度：所有的點數
  - linked list：鄰邊
    > 以線連接到的其他點
    
    > 不唯一，依據起點的不同，會有不同的linked list
    >> 鄰邊必須可以還原graph
    
#### Source
[Graph: Breadth-First Search(BFS，廣度優先搜尋)](http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)

[Graph: Intro(簡介)](http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html)

[🖋](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_12#content)

# Breadth-First Search
 > BFS：廣度優先搜尋，使用Level-Order Traversal
 >> 由起點開始，根據level一層一層走訪
 

 > traversal（走訪）graph之方法
 >> search（搜尋）的必要功能
 
 從起點開始，遍歷完整個graph，按照**就近原則**進行，距離起點相同的vertex其訪問順序是相近的
 
 
#### Step

從某一vertex出發，先走訪所有**相鄰**的vertex，再依序走訪與已走訪過的vertex相鄰但尚未走訪的vertex，直到所有相鄰的vertex都被走訪

![](https://buracagyang.github.io/2019/07/14/breadth-depth-first-search/BFS.gif)

- Step1：從頂點開始，即Level 0
- Step2：查找頂點以單線連接到的所有其他點，這些點即為Level 1
- Step3：假設所有Level 1的點為頂點，查找所有與Level 1以單線相連的其他點，這些點即為Level 2
- Step4：重複上述步驟，直到所有點都被走訪
  
#### Practice
 > by Queue
 
 > 當起點與鄰邊表相同時，走訪方式唯一

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_12/image/1576316336720.jpg)
> 無向圖：雙向，無指定特別方向，只要有線連結就要記錄

> graph資料結構：塞入資料就好
>> 無規定由大到小或由小到大：不唯一

使用queue紀錄print出的點所連接的其他點

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_12/image/output_aMJs9Q.gif)
> Queue中灰色部分，表示當次被提取的值

使用兩個array，一個處理queue，一個紀錄print出的順序

#### Source
[圖片來源](https://buracagyang.github.io/2019/07/14/breadth-depth-first-search/)

[BFS和DFS算法（第1讲）](https://www.youtube.com/watch?v=oLtvUWpAnTQ&t=)

[Breadth First Search (BFS) Algorithm](https://www.javatpoint.com/breadth-first-search-algorithm)

[Breadth first search](https://www.programiz.com/dsa/graph-bfs)

[橫向優先搜尋 (breadth-first search)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/bfs.html)

[BFS & DFS 學習整理](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/102866/)

[🖊](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_12#content)
