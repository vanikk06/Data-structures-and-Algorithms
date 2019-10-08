# Content
 - [Stack & Queue](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/weel_3#stack--queue)

# Stack & Queue
 > 儲存資料的方式
  - [Stack](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/weel_3#stack)
  - [Queue](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/weel_3#queue)
 
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
    
  [~🦑](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/weel_3#content)
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
   
  [🐙~](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/weel_3#content)
  
#### Source
 [Data Structures: Stacks and Queues](https://www.youtube.com/watch?time_continue=9&v=wjI1WNcIntg)


## Test min stack
[👉🏻HERE👈🏻](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/weel_3/Test%20min%20stack.py)
> following teacher's

資料結構：先進後出，取出必須要是`top`的資料
 - 利用`node`建立儲存空間（包含.val和.next），多加一個.min，配合要求
 - 將箭頭放在top那筆

#### Code
 - `__intit__`：min stack基礎的屬性設定
     - .topnode：ˋ在stack內top那筆資料
 - `push(x)`：增加一筆資料，變成新的top
   > 考慮stack內是否已有值存在
   - Yes：先將topnode.min存到暫存區，創建一個node存入x值成為topnode，再與暫存區內的值做比較
      - <：取代topnode.min
      - >=l：不動
   - No：創建一個node存入x值，成為topnode
 - `pop()`：取出top的資料，將下一筆資料成為新的top
 - `top()`：查看top那筆資料的值
 - `getMin()`：查看stack中最小的值


## Try min stack
> Using node
> Using array
