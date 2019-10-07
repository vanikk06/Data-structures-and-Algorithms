# Contents

# Stack & Queue
 > 儲存資料的方式
 
 ## Stack
  > 先進後出（LIFO：last in first out）
  
  疊盤子：優先處理最後發生的事
  - 使用地方：
    - 編輯器的undo（暫存上一步），關掉會清除暫存
    - 網頁的回到前一頁
    - 任何遞迴形式的演算法 e.g.走迷宮、[DFS(深度優先搜尋)](http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)
  - 功能：
    - `push(data)`：將data放進stack（放入）
    - `pop`：把「最上面」的data從stack中移除（取出）
    - `top`：回傳「最上面」的data（查看）
    - `IsEmpty`：確認stack裡是否有資料
    - `getSize`：回傳stack裡的資料個數
  
 ## Queue
  > 後進先出（FIFO：first in first out）
  
  排隊：按進入順序處理發生的事，不可從中插隊
  - 使用地方：
    - 安排多個程式的執行順序  e.g.作業系統（多個程式共享的資源，一次只能執行一個需求）
    - 演算法：
      - [BDS(廣度優先搜尋)](http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)
      - [Tree的Level-Order Traversal](http://alrightchiu.github.io/SecondRound/binary-tree-traversalxun-fang.html#level)
  - 功能：
    - `push(data)`/`InQueue`：將data從queue的「後面」放入，更新為新的back（放入）
    - `pop`/`DeQueue`：把front(最前面)的data從queue中移除，並更新front（取出、刪除）
    - `getFront`：頭的位置，回傳front所指的資料
    - `getBack`：尾的位置，回傳back所指的資料
      > 不能插隊，中間不走訪
    - `IsEmpty`：確認queue裡是否有資料
    - `getSize`：回傳queue裡的資料個數
   
  
#### Source
 [Data Structures: Stacks and Queues](https://www.youtube.com/watch?time_continue=9&v=wjI1WNcIntg)
