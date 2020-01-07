# Content
 - [Class notes](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_08#class-notes)
 - [Binary Tree](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_08#binary-tree)
 - [Full binary tree & Complete binary tree](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_08/README.md#full-binary-tree--complete-binary-tree)
 - [Try Binary Tree Level Order Traversal](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_08#try-binary-tree-level-order-traversal)
 - [Test Design binary tree](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_08#test-design-binary-tree)
 - [Try Design binary tree](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_08#try-design-binary-tree)
 
 
# Class notes
- toy code：寫完就可以丟掉的code

- 學習基礎知識：在應用端時，才有辦法判斷的標準
   > 目的是應用端的應用，但作為基礎的觀念必須清晰

[🍃](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_08#content)

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
- Edge：連結
- node：每個節點      
- subtree：
    - siblings（手足）：同階層的多個child
    - leaf node：自己一個，沒有child
- height of a node：從node到leaf node的edge數量
  > height of leaf node is 0.
 
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

#### Binary Tree 基本設定
- .val：儲存的值
- .left：左邊的child
- .right：右邊的child

> 範例Code
```python
class _Node:

   def __init__(self, element, parent=None, left=None, right=None):
      self._roof = None
      self._size = 0
      self._parent = parent    #記錄parent
      ``` 基本 ```
      self._element = element 
      self._left = left        
      self._right = right          
```

#### Create Binary Tree
 > add node
 
 > 範例Code
 ```python
 def _add_left(self, p, e):
   if node._left is not None: raise ValueError('Left child exists'):
      self._size += 1
      node._left = self._Node(e, node)
 ```

#### Source
[圖片來源](https://www.tutorialride.com/data-structures/trees-in-data-structure.htm)

[Binary Tree: Intro(簡介) - 學習Binary Tree的未來出路](http://alrightchiu.github.io/SecondRound/binary-tree-introjian-jie.html#application)

[Chapter 6. Trees II](http://www.math.bas.bg/~nkirov/2017/NETB201/slides/ch06/ch06-2.html)

[Binary Trees](http://cslibrary.stanford.edu/110/BinaryTrees.html#s1)

[Introduction to Tree Data Structure](https://www.youtube.com/watch?time_continue=1&v=ikPPdBDZnz4&feature=emb_logo)

#### Python 範例Code
[Python - Linked Lists](https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm)

[Python - Binary Tree](https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm)

[🌳](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_08#content)

# Full binary tree & Complete binary tree
  > 常見的 binary tree
  
#### Full binary tree
 > 又稱 Perfect binary tree
 
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_08/image/1574538305218.jpg) 
 
特性：
  - 所有內部node都有兩個child_node（subtree）
  - 所有leaf node具有相同的level（或相同的height）
    > leaf node：最底層的node
    
由上述性質可知道

若一個Full binary tree的leaf node之level為n，則整棵樹共有**2<sup>n</sup> - 1**個node

每個node與其child之關係：
> 第i個node
   - left child之index：2i
   - right child之index：2i + 1
   - parent之index：i/2 （取整數）
      > 除了root之parent為NULL

#### Complete binary tree
 > 不完備的Full binary tree

一棵binary tree的node按照Full binary tree的次序排列（由上至下、由左往右）

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_08/image/1574538183205.jpg)

#### Source
[Binary Tree: Intro(簡介)](http://alrightchiu.github.io/SecondRound/binary-tree-introjian-jie.html)

[🌵](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_08#content)

# Try Binary Tree Level Order Traversal
> LeetCode：102. Binary Tree Level Order Traversal

#### Source
[Google Coding Interview (2019) - Binary Tree Level Order Traversal (LeetCode)](https://www.youtube.com/watch?v=XZnWETlZZ14&feature=emb_logo)

[🌿](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_08#content)

# Test Design binary tree
  > Using teacher's linked list
  
[☘](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_08#content)
  
# Try Design binary tree

[🌴](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_08#content)
