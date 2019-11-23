
# Content



# NoneType

#### Source
[Python對<type ‘NoneType’>資料型別的處理](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/634089/)

#  Practice of class

#### Source
[python中，怎麼讓類返回值啊？](https://zhidao.baidu.com/question/504532877.html)

# Binary Search Tree
 > 應用於資料庫系統的原型
 
 ![](https://upload.wikimedia.org/wikipedia/commons/9/9b/Binary_search_tree_example.gif)
 
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
        > Undone
         - pre-order：一直往左邊走(小的)
         - post-order：一直往右邊走(大的)
         - in-order：按照input的順序，左右左右
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

[圖片來源](https://commons.wikimedia.org/wiki/File:Binary_search_tree_example.gif)

# Class notes
- **結構**目的：搜尋資料、效率important

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

# H.W.
- input:class

- insert: 與root比較，大的右邊，小的左邊
   > 遇到一樣的，擺左邊
   
- delete: 刪除所有值
   > 重新建構
   
   > 若delete到root，讓深度最小
   
- search:一樣的數字，與root最近的(level最top)
  > preorder:左邊先
- modify：全部修改


- insert & search:要有回傳值
   > 用我們的search去insert
- delete & modify:不用回傳值

#### Source
[資料結構 - 二元搜索樹(Binary Search Tree)](https://emn178.pixnet.net/blog/post/94574434)
