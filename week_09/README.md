
# Class notes


# Binary Search Tree
 > 應用於資料庫系統的原型
 
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
         - preorder：一直往左邊走(小的)
         - postorder：一直往右邊走(大的)
         - inorder：按照input的順序，左右左右
      - 查詢：find某個固定的值
         > 呼叫走訪
      - 刪除
         > 刪除點後，必須讓新連接的點維持Binary Search Tree架構
         >> 如何定義：刪除點後，維持Binary Search Tree架構
         
           - 有child
               - 一個child：
               - 兩個child：
           - 無child：直接砍掉


# input：值(存放數值 有重複)
delete
 > 原則：結構變化最少(取代值：從leaf最底層找)
 balance不會有大結構改變
 
 刪除值有parent，要跟perant
 
 若有重複值，可指定第一個遇到(設計定義)
 > binary tree：適合存唯一值(ID)

結構：搜尋資料、效率important


# input：ID(唯一值)
資料庫：儲存值會同時紀錄ID，刪除時不會有重複值問題


binary tree：最多兩個child
> tree不可以有loop

binary search tree：左右無法自己決定，全看與parent比較
>資料越亂愈越好，if整理後資料就是linked list

> 深度最小

1. 第一個值無條件是root
> 缺點：如果第一個是極端值，會變只有單邊(worse:O(n))

2.小於root放左邊，大於放右邊


紅黑樹：確保樹平衡
