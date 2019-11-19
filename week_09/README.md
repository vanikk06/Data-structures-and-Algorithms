
# Class notes

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
