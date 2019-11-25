# Content
- [Code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#code)
   - [Insert](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#insert)
   - [Search](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#search)
   - [Delete](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#delete)
   - [Modify](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#modify)
  
  
- [Jupyter notebook_The process of learning binary search tree](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/The%20process%20of%20learning%20binary%20search%20tree%20.ipynb)
    - [Jupyter nbviewer_The process of learning binary search tree](https://nbviewer.jupyter.org/github/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/The%20process%20of%20learning%20binary%20search%20tree%20.ipynb)

- [Jupyter notebook_Binary Search Tree功能說明](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/Binary%20Search%20Tree%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E.ipynb)
    - [Jupyter nbviewer_Binary Search Tree功能說明](https://nbviewer.jupyter.org/github/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/Binary%20Search%20Tree%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E.ipynb)


# Code
[🤜🏼HERE🤛🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/Binary%20Search%20Tree.py)

此次作業構思方式是採將現階段概念理解的內容，嘗試依造自己的想法逐步轉為執行步驟，過程再根據遇到的問題去進行調整、修正，直到測資結果符合預期

- 作業規則：
   1. 在已存在BST上，執行下列功能
   2. 回傳值為class
   3. 搜尋方式：深度優先（Depth-first）、前序pre-order（VLR）
   4. 數字可能為負數或重複
   5. 相同值，統一放左邊
   6. 修改、刪除需對所有相同值進行處理
   7. 搜尋返回含有target且離root最近的TreeNode
   8. 最終的BST結構，深度不可大於原本的深度
  
- Binary Search Tree（BST）特性：
   1. 每個node最多只能有兩個child
   2. left child必定小於、等於parent且right child 必定大於parent
   

- 反思：

   一開始思考的不夠完備，不是找到一般化的處理方式才開始打code，而是在過程將遇到的問題做出調整；解決的也僅有此次側資遇到的問題，若變換測資，不一定能達到預期效果（仍存在Bug）
   
   - 缺：
        1. 程式碼過長：判斷繁雜，排除目前問題方式採增加判斷式
            > BST向下增加一層，其可能結果是2的**指數成長**
        2. 考慮不夠完備：思考到的處理方式，無法涵蓋到所有可能範圍
        3. 時間不夠充分：在打這次作業的時候，剛好事情比較多，無妥善分攤導致作業製作的時間緊迫

## Insert
   > 新增、插入
   
   增加的val必須與root（parent）比較，大的放right，小的放left，若其位置已有node存在，就繼續往下一層比較，直到找到適當的放置位置
   
### Code
   > 採**遞迴**，執行重複的判斷動作
   
   先判斷root是否已經存在，若已存在再繼續往下執行
   
   接著判斷val是否有值輸入，有的話再往下進行判斷
   - val是否小於等於root的值：
      - Yes：判斷root的left child是否已有node存在
         > 放left child
          - Yes：呼叫自己，以已存在的left child作為parent，往下一層繼續看
          - No：在left child的地方創造一個node
      - No：判斷root的right child是否已有node存在
         > 放right child
          - Yes：呼叫自己，以已存在的left child作為parent，往下一層繼續看
          - No：在left child的地方創造一個node
          
   - 回傳新增的node
   
#### Problem

問題3：回傳值並非node而是None
> return設置錯誤，回傳的結果並非是設置的回傳值，而是無設置回傳值的結果
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/image/1574665280253.jpg)

因為return是放在if else中間，在第一次判斷的時候，如果左邊/右邊已有node存在，就會進入else執行遞迴，遞迴會記憶上一步尚未執行的動作，所以在找到創立的node位置的之後，會因為返回上一步的動作，覆蓋掉return的回傳值

#### P.S.
再完成Search後，有想要嘗試利用指標移動的方式來達到Insrt，因為以pointer移動的方式進行判斷，不會增加空間複雜度，但因為時間緊迫就暫時作罷
   
   
[🔸](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#content)

## Search
   > 搜尋、走訪
   
   尋找值為target的node，若有重複值，則選擇距離root最近的node。判斷方式依然與BST相同，若target大於root（parent）就往right child走；若小於、等於，就往left child走
   
#### Code
   > 使用**指標**的方式，執行重複的判斷動作
   
   > 注意！node.val不可為None，移動時必須確保移動目標已有node存在，
   否則會出現`AttributeError: 'NoneType' object has no attribute 'val'
`
   
   先判斷root是否已經存在，若已存在再繼續往下執行
   
   建立一個pointer指標，從root開始進行移動
   
   - 指標的值是否與target相同
      - No：
         - target小於指標內的值，而且指標的left child已存在
            >往指標的left child移動
         - target大於指標內的值，而且指標的right child已存在
            >往指標的right child移動
         - 不滿足上面兩個的條件：跳出Search
            > target不存在BST內
      - Yes：回傳指標指到的node
   
   
   
[🔹](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#content)

## Delete
   > 刪除
   
   刪除一個或多個（重複值）存在於BST內的node，且刪除後仍要符合BST基本特性

#### Code
   > 執行較為複雜，採**指標**移動與多個**套件組合**
   
   > 目標：讓BST變動最小
   >> 若存在重複值，則從最底層的node開始刪除
   
 可能情況：
   1. 沒有child：直接刪除
   2. 有一個child：改變node的連結，讓目標刪除的child與目標刪除的parent建立新的連結
   3. 有兩個child
    
    
   起初，程式碼設計：
      - 想讓BST變動變小，因此刪除時從**最底層**的node開始進行
      - 若目標刪除node存在child
   
   
   - `_delete_pointer`：找到要刪除的目標node
      - pointer：移動指標
         > 想要從最底層開始刪除node，就必須走訪到最底層
      - pre_pointer：移動指標之parent
         > 刪除方式為**重建連結**，因此必須把目標刪除node之parent也記錄下來
      - i：target存在的個數
         > 遇到pointer指標的值與target相同時，就+1
      - delete_node：刪除指標
         > 遇到pointer指標的值與target相同時，就將其記錄到delete_node指標內
         
         > 若存在重複值，重新指派時會覆蓋上去
      - pre_delete_node：刪除指標之parent
      
      pointer指標要從root走到最底層，因此設計一個while迴圈，若pointer指標有child存在，就進入迴圈，否則跳出迴圈
     
      - pointer有left child或有right child：
         - target等於pointer的值
         - target小於pointer的值，且pointer的left child存在
            > 注意！node必須存在才可移動
            
            pointer指標往left child移動
         - target大於pointer的值，且pointer的right child存在
            > 注意！node必須存在才可移動
            
            pointer指標往right child移動
         - 不滿足上述任何條件：休息不做任何動作
            >　target不存在於BST內
    
   

[🔶](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#content)

## Modify
   > 修改

[🔷](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#content)
