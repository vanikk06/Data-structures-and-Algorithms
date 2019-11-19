# Class notes
- toy code：寫完就可以丟掉的code

- 學習基礎知識：在應用端時，才有辦法判斷的標準
   > 目的是應用端的應用，但作為基礎的觀念必須清晰

# Binary Tree
 > 儲存資料的方法
 
 > 增加搜尋效率
 
- 處理資料：seach、sort
- 儲存資料、資料結構：linked list、stack、queue、heap

#### Tree points

![](https://www.tutorialride.com/images/data-structures/structure-of-tree.jpeg)

- root：樹的頂端，只會有一個
   - 底下可長出子節點（child）
      > 若child的parent不是root，則此 parent＆child 稱之為子樹（subtree）
- Edge：連結點
- node：每個節點      
- subtree：
    - siblings（手足）：同階層的多個child
    - leaf node：自己一個，沒有child
    
- Binary Tree：每一個node，最多只有兩個child
  > 二元樹：Tree's special cass
  
     - heap：讓list符合heapity規範
         > 限制root樣子
          - Max heap
          - min heap
          
#### 與linked list相似
 - node：空間
      - .value：儲存的資料
      - .next：指向下一個node的pointer
        > 轉為tree，將next拆成兩半，改為left、right
       
 - Tree功能：
      - 查詢：
        - len、is_empty
        - root
        - parent(x)
        - left(x)
        - right(x)
        - sibling(x)
        - children(x)
        - depth(x)：深度
          > 由上往下
        - height：高度
          > 由下往上
        - is_root(x)：是否是最上層的node
        - is_leaf(x)：是否是最後一層的node
  
      - 插入、新增（建構結構）：
           - add_root(x)
           - add_left(x, y)
           - add_right(x, y)
           - replace(x, y)：取代，增加在已存在值的位置
           - delete(x)
           - attach(x, t1, t2)：合併兩棵subtree，從哪個點開始合併（合併點）
           
> 定義node，可增加.parent：記錄parent （此功能用走訪也可達到）

>> 優：可減少走訪parent的函式

>> 缺：每個node都很肥

#### Source
[圖片來源](https://www.tutorialride.com/data-structures/trees-in-data-structure.htm)

[Binary Tree: Intro(簡介) - 學習Binary Tree的未來出路](http://alrightchiu.github.io/SecondRound/binary-tree-introjian-jie.html#application)

[Chapter 6. Trees II](http://www.math.bas.bg/~nkirov/2017/NETB201/slides/ch06/ch06-2.html)
