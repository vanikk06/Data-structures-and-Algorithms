
# Stack & Queue
 > 儲存資料的方式
 
 ## Stack
  > 先進後出（LIFO：last in first out）
  
  疊盤子：優先處理最後發生的事
  - 使用地方：
    - 編輯器的undo（儲存上一步）
    - 網頁的回到前一頁
    - 任何遞迴形式的演算法
  - 功能：
    - `push(data)`：將data放進stack（放入）
    - `pop()`：把「最上面」的data從stack中移除（取出）
    - `top()`：回傳「最上面」的data（查看）
    - `IsEmpty`：確認stack裡是否有資料
    - `getSize`：回傳stack裡的資料個數
  
 ## Queue
  > 後進先出（FIFO：first in first out）
  
  排隊：
