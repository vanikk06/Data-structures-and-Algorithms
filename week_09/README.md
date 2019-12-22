
# H.W.3_Binary Search Tree
[🤜🏼HERE🤛🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree)
  - [Code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#code)
     - [Insert](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#insert)
     - [Search](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#search)
     - [Delete](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#delete)
     - [Modify](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#modify)
  
  
- [Jupyter notebook_The process of learning binary search tree](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/The%20process%20of%20learning%20binary%20search%20tree%20.ipynb)
    - [Jupyter nbviewer_The process of learning binary search tree](https://nbviewer.jupyter.org/github/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/The%20process%20of%20learning%20binary%20search%20tree%20.ipynb)

- [Jupyter notebook_Binary Search Tree功能說明](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/Binary%20Search%20Tree%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E.ipynb)
    - [Jupyter nbviewer_Binary Search Tree功能說明](https://nbviewer.jupyter.org/github/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/Binary%20Search%20Tree%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E.ipynb)


# Content
  - [UnboundLocalError](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/README.md#unboundlocalerror)
  - [is vs. ==](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/README.md#is-vs-)
  - [NoneType](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#nonetype)
  - [Depth-First Search](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#depth-first-search)
  - [Traversal in Binary Tree](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#traversal-in-binary-tree)
  - [Binary Search Tree](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#binary-search-tree)
  - [Class notes](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#class-notes)
  - [Practice of Binary Search Tree](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#practice-of-binary-search-tree)

# UnboundLocalError
  > 未綁定區域錯誤
  >> 作用域問題：像是local裡面出現not defined的error
  
此error會出現，是因為在local（區域）內，python無法參照（reference）到此變數\
（可能在local內出現重新賦值此變數的動作，因為是在local內所以python會判定是一個新的變數，然而在local內找不到此變數被賦值（assignment）的動作，從而找不到其記憶體的位置）

一般解決此問題，會在變數前加上`global`來定址，讓python到全域去找到它的記憶體位置

#### 觀念
- python是函數(function)式語言, 函數的意義如同變數, 在函數中的**變數範圍僅及於函數的範圍**
- python並無變數宣告(declaration)的機制, 必須透過「等號」對變數**賦值(assignment)在記憶體中定址**

#### Source
[python的作用域問題](https://segmentfault.com/q/1010000006716248/a-1020000006720179)

[python exceptions.UnboundLocalError(已解決)](https://ithelp.ithome.com.tw/questions/10185944)

[🌚](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#content)

#  is vs. ==

Python物件包含三要素：
  - id：**唯一**標識一個物件
  - type：物件的型別
  - value：物件的值
  
is：通過**id**判斷，a物件是否就是b物件

==：通過**value**判斷，a物件的值是否和b物件相等

#### Source
[Python對<type ‘NoneType’>資料型別的處理](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/634089/)

[🌗](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#content)



# NoneType
  > python內一個特殊型別

Python：物件導向
  > 物件 = 屬性 + 方法
  - 基本資料類型：布林型別、整型、浮點型、字串、列表、元組（tuple）、集合、字典...
  
NoneType物件，只有一個值**None**
  > 可將None複製給任何變數，但不能建立其他NoneType物件
  - 不支援任何運算、也沒有任何內建方法
  - None和其它的資料型別比較，永遠返回False
  
None：值，表示一個**空物件**
  >　不可理解為0，0是有意義的，而None是特殊的空值
  
  
#### 變數判斷是否為None
   > None、False、" "（空字串）、0、[ ]（空列表）、{ }（空字典）、( )（空元組），都相當於False
    
- 第一種：`if x is None`
- 第二種：`if not x`
- 第三種：`if not x is None`
  > 理解：`if not (x is None)`

#### Source
[Python對<type ‘NoneType’>資料型別的處理](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/634089/)

[🌖](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#content)

# Depth-First Search
  > 深度優先搜尋法（DFS）
  >> 核心精神：如同Pre-Order Traversal：**先遇到的vertex（頂點）就先Visiting**，並且以先遇到的vertex做為新的搜尋起點，直到所有"有edge相連的vertex"都被探索過
 
 是一種用來遍尋一個樹（tree）或圖（graph）的演算法。由root（或graph上的某一點）來開始搜尋，先探尋edge上未搜尋的node/vertex，並**盡可能深的搜尋**，直到該node所以edge上的node都以探尋，就**回溯（backtracking）**到前一個node，重複探尋未搜尋的node，直到找到目標node或遍尋全部node
 
 - Pre-Order Traversal：每一組「Current-left-right」必定是Current
 node先Visiting，接著是left child，最後才是right child
 - 盲目搜尋（uninformed search）：只要有路就繼續往前走，但不保證是最短路徑
   > e.g.迷宮問題（maze problem）
 - 本質上是一種**遞迴結構**，而遞迴結構其實是利用了系統的**Stack**

#### Source
[Graph: Depth-First Search(DFS，深度優先搜尋)](http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)

[深度優先搜尋法
(Depth-first Search)](http://simonsays-tw.com/web/DFS-BFS/DepthFirstSearch.html)

[🌑](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#content)


# Traversal in Binary Tree
  > 尋訪
  > Binary Tree：node的pointer為二維（left、right）
  
- Traversal：站在A地，往所有與A地相連的地方移動
  > 在此，以pointer實現，站在node（A）上，並且node（A）具有指向node（B）之pointer，便能夠由A往B移動
  
- Visiting：移動到特定的node之後，對其進行的動作
  > e.g.print out（顯示資料）、assign（賦值）、刪除資料等等

#### Traversal方式

假設現在CurrentNode位在A，leftchild與rightchild分別是B和C，且加上一條限制「L一定在R之前」，能產生三種相對關係：

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/image/1574627120689.jpg)

- Pre-Order（VLR）：當CurrentNode移動到A時，先對A進行Visiting，接著前往left child，在前往right child
  > 先遇到的node就先Visiting
  
  > 若child指向None則忽略
- In-Order（LVR）：當CurrentNode移動到A時，先對A的left child進行Visiting，接著回到A，再前往right child
   > 若child指向None則忽略
- Post-Order（LRV）：當CurrentNode移動到A時，先對A的left child進行Visiting，接著前往right child，再回到A
   > 若child指向None則忽略
   
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/image/1574628759524.jpg)
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/image/1574628411593.jpg)
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/image/1574628584718.jpg)

#### Source
[Binary Tree: Traversal(尋訪)](http://alrightchiu.github.io/SecondRound/binary-tree-traversalxun-fang.html)

[🌒](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#content)

# Binary Search Tree
 > 應用於資料庫系統的原型
 
 > 放置大量數字並進行排序的資料結構
 
 ![](https://upload.wikimedia.org/wikipedia/commons/9/9b/Binary_search_tree_example.gif)
 
|  | Best | Worst |
| --- | --- | --- |
| **Time complexity** | O(log n) | O(n) |
 
- Binary Tree：僅有**兩個**子節點
  > 建構：讓資料insert後能維持只有兩個child，且insert後指到新的node
  >> 可自行指定要放left或right
  
- Binary Search Tree：
   - 僅有兩個child
   - 不可自行指定add_left或add_right，insert位置要符合架構
   - 功能
      - 新增：與root(parent)比較，大的放right，小的放left
        > 判斷式
      - 走訪
        > 遇到一樣的
         - pre-order：一律放左邊(小的)
         - post-order：一律放右邊(大的)
      - 查詢：find某個固定的值
         > 呼叫走訪
      - 刪除
         > 刪除點後，必須讓新連接的點維持Binary Search Tree架構
         >> 如何定義：刪除點後，維持Binary Search Tree架構
         
           - 有child
               - 一個child：child要與new_parent比較（大的接右邊，小的接左邊）
               - 兩個child：要以誰取代？
                 > 讓取代條件變動愈少愈好
           - 無child：直接砍掉
         
- Binary Tree vs. Binary Search Tree
  - Binary Tree：set
  - Binary Search Tree：subset
    > 多的條件：無法自行決定left或right

#### Source
[Binary Search Tree library in Python](https://www.laurentluce.com/posts/binary-search-tree-library-in-python/)

[Python: Binary Search Tree - BST](https://www.youtube.com/watch?v=YlgPi75hIBc&feature=youtu.be)

[Binary Tree and Binary Search Tree in Data Structure](https://www.youtube.com/watch?v=7vw2iIdqHlM&feature=emb_logo)

[Binary Search Tree](http://www.csie.ntnu.edu.tw/~u91029/Order.html)

[圖片來源](https://commons.wikimedia.org/wiki/File:Binary_search_tree_example.gif)

[🌓](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#content)


# Class notes
- **結構**目的：搜尋資料、效率important

[🌔](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#content)

# Practice of Binary Search Tree

- Binary Tree：最多兩個child
  > tree不可以有loop

- Binary Search Tree：左右無法自己決定，全看與parent比較
  > 資料越亂愈越好，若資料是整理好的，那就會是linked list
   1. 第一個值無條件是root
      > 缺點：如果第一個是極端值，會變只有單邊(worse:O(n))

   2. 小於root放左邊，大於放右邊

- input
    - 值
      > 存放數值，可能會有重複
    - ID(唯一值)
      > 資料庫：儲存值會同時紀錄ID，刪除時不會有重複值問題

- delete
  > 原則：結構變化最少(取代值：從leaf最底層找)
  >> balance不會有大結構改變
  - 刪除值後，若其本身有parent，要讓新連接值與perant比較
  - 若有重複值，可指定第一個遇到(定義設計)
   > Binary Search Tree：適合存唯一值(ID)

- 紅黑樹：確保樹平衡

#### Source
[Binary Search Tree: Search(搜尋資料)、Insert(新增資料)](http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html)

[GitHub -  jakemmarsh/binarySearchTree.py](https://gist.github.com/jakemmarsh/8273963)

[資料結構 - 二元搜索樹(Binary Search Tree)](https://emn178.pixnet.net/blog/post/94574434)

[🌕](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#content)


# Try Print Binary Tree
  > LeetCode：655. Print Binary Tree
[🌝](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09#content)
