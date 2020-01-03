# Content
- [Code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#code)
  - [Insert](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#insert)
  - [Search](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#search)
  - [Delete](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#delete)
  - [Modify](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#modify)

- [Adjustment of code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#adjustment-of-code)
  - [Optimization of Insert](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#optimization-of-insert)
  - [Adjustment of Delete](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#adjustment-of-delete)
   
- [Jupyter notebook_The process of learning binary search tree](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/The%20process%20of%20learning%20binary%20search%20tree%20.ipynb)
  - [Jupyter nbviewer_The process of learning binary search tree](https://nbviewer.jupyter.org/github/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/The%20process%20of%20learning%20binary%20search%20tree%20.ipynb)

- [Jupyter notebook_Binary Search Tree功能說明](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/Binary%20Search%20Tree%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E.ipynb)
  - [Jupyter nbviewer_Binary Search Tree功能說明](https://nbviewer.jupyter.org/github/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/Binary%20Search%20Tree%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E.ipynb)


# Code
[🤜🏼HERE🤛🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/Adjustment%20of%20Binary%20Search%20Tree.py)

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
   
   - 缺點：
        1. 程式碼過長：判斷繁雜，排除目前問題方式採增加判斷式
            > BST向下增加一層，其可能結果是2的**指數成長**
        2. 考慮不夠完備：思考到的處理方式，無法涵蓋到所有可能範圍
        3. 時間不夠充分：在打這次作業的時候，剛好事情比較多，無妥善分攤導致作業製作的時間緊迫

[🔘](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#content)

## Insert
   > 新增、插入
   
   增加的val必須與root（parent）比較，大的放right，小的放left，若其位置已有node存在，就繼續往下一層比較，直到找到適當的放置位置
   
#### Code
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
#### Demo
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/image/1574686627812.jpg)

#### Problem

- 問題3：回傳值並非node而是None
> return設置錯誤，回傳的結果並非是設置的回傳值，而是無設置回傳值的結果
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/image/1574665280253.jpg)

因為return是放在if else中間，在第一次判斷的時候，如果左邊/右邊已有node存在，就會進入else執行遞迴，遞迴會記憶上一步尚未執行的動作，所以在找到創立的node位置的之後，會因為返回上一步的動作，覆蓋掉return的回傳值

- 回傳值錯誤
   > `return TreeNode(val)`回傳的是一個新的node，其並無與root連結
   ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/image/1574765983358.jpg)
   
- 更改上面的「回傳值錯誤」後，會出現`UnboundLocalError`
   > `UnboundLocalError`：此錯誤是因為遞迴結束時，會一層一層往回退，當回到最初並返回node時，此時python會因為在最初node尚未被賦值的原因，而無法參照node（找不到它記憶體的位置）
   ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/image/Snipaste_2019-12-22_04-52-43.png)
   >> 在此解決，是在使用遞迴的地方，先將node定址，讓python可以找到其記憶體的位置

#### P.S.
再完成Search後，有想要嘗試利用指標移動的方式來達到Insrt，因為以pointer移動的方式進行判斷，不會增加空間複雜度，~但因為時間緊迫就暫時作罷~，此部分已完成，在[Optimization of insert](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#optimization-of-insert)
   
   
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
   
#### Demo
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/image/1574686779337.jpg)
   
[🔹](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#content)

## Delete
   > 刪除
   
   > 刪除後，不可大於原本的BST深度
   
   刪除一個或多個（重複值）存在於BST內的node，且刪除後仍要符合BST基本特性

#### Code
   > 執行較為複雜，採**指標**移動與多個**套件組合**
   
   > 目標：讓BST變動最小
   >> 若存在重複值，則從最底層的node開始刪除
   
可能情況：
   1. 沒有child：直接刪除
   2. 有一個child：改變node的連結，讓目標刪除的child與目標刪除的parent建立新的連結
   3. 有兩個child：將目標刪除node的值用child覆蓋，往下移動，直到指到僅剩一個child的node
      - 若目標刪除node在root右邊，就用right child覆蓋
      - 若目標刪除node在root左邊，就用left child覆蓋
    
    
 起初，程式碼設計：
   > `_delete_pointer`、` _delete_action`
   - 想讓BST變動變小，因此刪除時從**最底層**的node開始進行
   - 目標刪除node可能存在child，依照各自情況，執行適當的刪除程序
 
 再完成上述的程式碼後，才想到沒有考慮到如果目標刪除node是root的情形，再此情形不適合使用原本的刪除步驟（因為決定在有兩個child的情況下，覆蓋值要用left child還是right child的判斷依據，是看delete_node指標的位置是在root左邊還是右邊），因此另外設計一個目標刪除node為root的刪除程序
   > `_delete_root`
   
----------------------------------------------------------------------------------------------------------------------------------------     
   - `delete`：刪除所有存在BST上的目標刪除node
      - 先呼叫`_delete_pointer`找出第一個目標刪除node之parent、目標刪除node與target存在個數
      - 如果i不等於0：進入刪除的程序
         > BST內存在目標刪除node
         - 目標刪除node是root：呼叫`_delete_root`進行刪除，並回傳其結果
         - 目標刪除node不是root：依照target存在個數的次數重複，呼叫`_delete_action`進行刪除，再將從刪除後的BST重新尋找下一個目標刪除node
            > 🐛，沒有考慮到若下一個目標刪除node是root，要使用`_delete_root`的狀況
      - 回傳：完成刪除後的BST
            
   
   - `_delete_pointer`：找到要目標刪除node
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
     
      - pointer有left child或有right child，進入while迴圈：
         - target等於pointer的值：將此時的pointer指標存入delete_node指標內，並將i+1。
            > 🐛，應將 `target == pointer.val`更改為`target == pointer.val and pointer.left != None`
            
            pointer指標往left child移動
         - target小於pointer的值，且pointer的left child存在：pointer指標往left child移動
            > 注意！node必須存在才可移動        
         - target大於pointer的值，且pointer的right child存在：pointer指標往right child移動
            > 注意！node必須存在才可移動          
         - 不滿足上述任何條件：休息不做任何動作
            > target不存在於BST內
         
        當跳出while迴圈時，pointer指標必定指在leaf node
         - leaf node的值是否與target相同：
            - Yes：將此時的pointer指標存入delete_node指標內，並將i+1。
         - 回傳：目標刪除node之parent、目標刪除node與target存在個數
   
   - `_delete_action`：進行刪除的動作，要將三種小孩情形考慮進來
      > 考慮不夠完備，判斷是並非一般化的式子
      - 沒有child：無後顧之憂，可以直接刪除
           - 目標刪除node小於其parent：parent的left child指向None
           - 目標刪除node大於其parent：parent的right child指向None
      - 一個child：要將目標刪除node之parent與目標刪除node的child建立連結         
           - 目標刪除node是right child：將其right child的值與其parent比較
              > ❌，此處判斷多餘，刪除目標之right child其值必定大於刪除目標之parent
              - right child的值小於、等於parent的值：將right child建立連結在parent的left
              - right child的值大於parent的值：將right child建立連結在parent的right
           
           - 目標刪除node是left child：將其left child的值與其parent比較
              > ❌，此處判斷多餘，刪除目標之left child其值必定小於、等於刪除目標之parent
              - left child的值小於、等於parent的值：將left child建立連結在parent的left
              - left child的值大於parent的值：將left child建立連結在parent的right
           
      - 兩個child：覆蓋，移動，直到delete_node指標指到僅有一個child的node
      
         建立一個while迴圈，若delete_node指標仍有兩個child，就進入迴圈
         > 在while迴圈內，delete_node指標必定有兩個child
           - 若目標刪除node在root左邊：用left child覆蓋目標刪除變數，並把delete_node指標指到left child
           - 若目標刪除node在root右邊：用right child覆蓋目標刪除變數，並把delete_node指標指到right child
           
          當跳出while迴圈時，delete_node指標必定指到僅有一個child或沒有child的node
           - 沒有child：無後顧之憂，可以直接刪除
              - 目標刪除node小於其parent：parent的left child指向None
              - 目標刪除node大於其parent：parent的right child指向None
           - 一個child：
             > 🐛，此時要重新建立連結的parent，因為前面覆蓋的動作，導致child不必然大於/小於、等於parent，因此建立連結時，要考慮目標刪除node之parent是否有其他的child存在
              - 目標刪除node是其parent的left child
                  - 目標刪除node是left child：將left child建立連結在parent的left
                  - 目標刪除node是right child：將right child建立連結在parent的left
                     > ❌，應該建立在parent的right
                     >> 因為此時的parent，就是原本parent
              - 目標刪除node是其parent的right child
                  - 目標刪除node是left child：將left child建立連結在parent的right
                     > ❌，應該建立在parent的left
                     >> 因為此時的parent，就是原本parent    
                  - 目標刪除node是right child：將right child建立連結在parent的right
      - 迴傳：刪除掉所有target的BST
                     
   - `_delete_root`：目標刪除node為root
      > 若要讓刪除root對BST造成的變動最小，可考慮以left_subtree的最大值或right_subtree的最小值取代，在此採**left_subtree的最大值**
      
      - Max：left_subtree最大值的指標，從root的left child開始
      - pre_Max：left_subtree最大值指標之parent
      
      建立一個while迴圈，讓Max指標移動到left_subtree最大值的位置
      > Max指標從root的left child開始
      
      > 若為left_subtree的最大值，則其必定存在於最右邊的right child
      - Max的指標，是否存在right child
         - Yes：Max往right child移動
         
      當跳出while迴圈時，Max指標必定指到left_subtree最大值的位置，在此有兩種情況：
      1. root的left child本身就是最大值
      2. 最大值存在於left_subtree最右邊的right child
      
      - 在情況1：直接將root的left child覆蓋掉root，並重新建立root與root的left child的left child之連結
      
      - 情況2，要進一步判斷Max指標是否有child存在
         > 若其存在child，則必定為left child
         - 沒有child：用Max指標的值覆蓋掉root，並將Max指標之parent的right child指向None
         - 有一個child：用Max指標的值覆蓋掉root，並將Max指標之parent的right child指向Max指標的left child
       - 迴傳：刪除掉root的BST
     
#### Demo
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/image/1574686676856.jpg)
   

[🔶](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#content)

## Modify
   > 修改
   >> 👎🏻
   
   更改已存在於BST內node的值，並讓更改後的BST符合其特性
   
#### Code
   > 注意！修改後的BST其深度不能大於原本的深度
   
   對modify的設計概念是最模糊的，再思考過後，針對非root的目標修改node，決定採取兩種方式：
   - 方法1：若目標修改node的變動幅度，不需要變動到其parent，則採此方法
      > 僅為目標修改node之subtree的區域變動
      >> e.g.left child的變大幅度，不會大於其parent；right child的變小幅度，不會小於其parent
      
      > But，後來時間不夠，並無完成此種方法
   - 方法2：若目標修改node的變動幅度，會變更到其parent，則採刪除，重新插入的方式
   
   
------
   - `modify`
      > target：原始值
      > new_val：目標變更值
   
      - 如果target在root的右邊，且new_val與root的值相同
         > 因為重複值必須放在左邊，因此將原本比root大的target修改為與root值相同時，無條件必須刪除重新插入
         先全部刪除，之後在根據原本target存在的個數，決定插入new_val的次數，最後回傳修改後的BST
      - 目標修改node不是root：將target全部刪除後，在依據其原本存在的個數，決定插入new_val的次數，回傳修改後的BST
      - 目標修改node是root
         - new_val介於root的left child與rigth child之間：直接修改
            > 在new_val介於原本root的left child與right child的情況下，直接修改root不會對BST的性質造成影響，但要考慮重複值存在的問題
            - new_val是否大於target
               > 如果原本BST就有new_val的node，因為target < new_val，所以其會存在於right_subtree，要將其改為放在left_subtree
               - Yes：將其刪除，重新插入
         - new_val不介於root的left child與rigth child之間：刪除root後，重新插入
            
   - `_modify_method`：方法2，刪除目標修改node
      > 調整delete，回傳值增加"target存在的個數"
   - `_modify_root_delete`：目標修改node為root，且target < new_val的刪除程序
      > 要在right_subtree內找到與new_val相同值的node，將其刪除
      
 

#### Demo
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/image/1574686740770.jpg)


[🔷](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#content)


# Adjustment of code
更改或優化Binary Search Tree的程式碼

- [Optimization of Insert](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#optimization-of-insert)

## Optimization of Insert
> 將尋找node的方式，由遞迴改為指標
>> 使用指標的方式，空間複雜度會較低

[🤜🏼HERE🤛🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/Optimization%20of%20insert.py)

在BST增加一個node，並讓BST維持其架構

val小於、等於root放左邊，大於root放右邊，若已經有node存在，則將其作為parent，往下繼續找
 
#### Code
> 指標

先判斷root是否已經存在
   - Yes：返回
   - No：繼續往下執行，建立一個pointer指標放入root，並建立一個空的node變數給後面操作

接著判斷val是否有值輸入，有的話再往下進行判斷
   - 使用while迴圈判斷node是否是空的
      > node：放入新增的node
      - Yes：將input的val與pointer指標的val做比較
         - 小於、等於：
            - left child是否已有node存在
               - Yes：pointer指標往左邊移動
               - No：在此位置創造一個新的node，並存入node變數中
         - 大於：
            - right child是否已有node存在
               - Yes：pointer指標往右邊移動
               - No：在此位置創造一個新的node，並存入node變數中
      - No：回傳node變數
     

[🔴](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#content)

## Adjustment of Delete
   > 調整一些錯誤跟多餘的程式碼

[🤜🏼HERE🤛🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/Adjustment%20of%20delete.py)

將原本delete程式碼內有問題的部分進行更改，但在「有兩個孩子」的刪除狀況還沒有想到較好的方法，仍未更改

#### Code
   > 此處僅更改部分

- `delete`：刪除所有存在BST上的目標刪除node
   > 原本若存在root的重複值時，刪除的動作僅會採用`_delete_action`，不會進入`_delete_root`
   
   先呼叫`_delete_pointer`找出第一個目標刪除node之parent、目標刪除node與target存在個數\
   
   用for迴圈，來重複執行刪除動作
    > 若i = 0則for迴圈不會執行
     
     - 先判斷目標刪除node是否是root
         - Yes：呼叫`_delete_root`進行刪除，並回傳其結果
            > 當刪除到root，若其存在重複值，root的刪除一定是最後一個動作，所以可以直接回傳
         - No：呼叫`_delete_action`進行刪除
     - 回傳：完成刪除後的BST
   
- `_delete_pointer`：找到目標刪除node

   僅更改在while迴圈內，target等於pointer的值的判斷，讓其完備

- `_delete_action`：進行刪除的動作
   
   刪掉多餘的判斷式
   
   在「兩個孩子」的情況下，跳出while迴圈時，還存在一個child的bug仍未解決，嘗試了許多方法，目前都還沒有成功

[🔵](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#content)
