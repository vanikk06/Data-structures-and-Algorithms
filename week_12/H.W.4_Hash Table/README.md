# Content
  - [Jupyter notebook_The process of learning hash table](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_12/H.W.4_Hash%20Table/The%20process%20of%20%20learning%20hash%20table.ipynb)
    - [Jupyter nbviewer_The process of learning hash table](https://nbviewer.jupyter.org/github/vanikk06/Data-structures-and-Algorithms/blob/master/week_12/H.W.4_Hash%20Table/The%20process%20of%20%20learning%20hash%20table.ipynb)
  - [Notes](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_12/H.W.4_Hash%20Table#notes)
  - [Error](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_12/H.W.4_Hash%20Table#error)
  - [Code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_12/H.W.4_Hash%20Table#code)
  - [Demo](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_12/H.W.4_Hash%20Table#demo)



# Notes
##### [MD5套件](https://kite.com/python/examples/2084/crypto-generate-a-new-md5-hash)
  - 宣告物件時，要先`.new()`一個初始的
  - 塞物件`.update`：這物件裡面要開始轉換
    > 要告訴它編碼為何`.encode("utf-8")`，無此會Error
    
    > 轉出來16進位，要再轉為10進位(not正規)
    
操作時，可採用
 ```python
 h = MD5.new()
 h.update("input".encode('utf-8'))
 ```
或是
 ```python
 h = MD5.new("input".encode('utf-8'))
 ```
不可將`h = MD5.new()`與`h.update("input".encode('utf-8'))`分開執行
  > 在重複執行`h.update("input".encode('utf-8'))`但未執行`h = MD5.new()`的情況下，初始值會改變，從而導致hash value改變
 

#### practice
  - capacity：容量，可變動
      > array長度
  - 包函式
    - 走訪linked list：增加、刪除、尋找
      > 新增可增加一次就好
    - 呼叫編碼
  - array內儲存linked list，index由MD5決定
  - linked list內儲存int


# Error

### TypeError
 > `missing 1 required positional argument`
 
在使用class建立物件（例項化）時，要先呼叫class，使用class名稱，後面必定要加()，否則會出現此TypeError

#### Source
[問題Missing 1 required positional argument引出的關於python例項化的經驗教訓](https://www.itread01.com/content/1544325485.html)

### IndexError
  > `list assignment index out of range`

index不存在array中，操作的index超過範圍

### AttributeError
  > `'NoneType' object has no attribute 'val'`
  
❗ 移動node指標，若判斷式採**val**，要小心是否會移到None ❗
  
目標刪除值不存在，因為其移動的判斷只要值與目標刪除val不同就往下跑，因此會跑到None去判斷它的val，從而錯誤

#### Source
[LeetCode介紹](https://arton0306blog.wordpress.com/2018/04/15/leetcode%E4%BB%8B%E7%B4%B9/)

# Code
  > 使用兩個class，一個MD5套件
  
[🤜🏾HERE🤛🏾](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_12/H.W.4_Hash%20Table/H.W.4_Hash%20Table.py)

缺點：思慮不夠完備，沒有考慮到所有情形

✔Status：Runtime Error
   > 執行期錯誤，通常是access（訪問）到陣列外面
   >> remove：目標刪除值不存在時會出現`AttributeError: 'NoneType' object has no attribute 'val'`
   
🚫 Status：Time Limit Exceeded
   > 時間複雜度過高，要精簡程式碼
   >> 此處未更改，以防程式碼相似度過高
   

透過MD5將字串轉換為編碼，在決定其於array內的位子，再將其以node的方式加入array中
> 多個相互連結的node稱之為linked list
>> 此為單向連結

#### ListNode
- `__init__`：linked list基本屬性
  - .val：node內儲存的資料
    > int
  - .next：指向下一個node的連結
    > ListNode
  
#### MyHashSet
- `__init__`：hash table基本屬性
  - .capacity：容量，array長度
    > int
  - .data：建立array，以便在特定的array[index]內儲存資料
  
- `Encoding_MD5`：透過MD5將input進行編碼化
  - 使用MD5套件進行編碼
  - encoding_key：將編碼以十六進位表示，再轉成十進位
  - index：將encoding_key除以array的長度，找到存放的位置

- `add`：增加資料
 
  使用`Encoding_MD5`將要增加的資料進行編碼
  - 先判斷目標存入位置是否已有值存在
    - No：在目標存入位置創造一個node，存入編碼
    - Yes：將已存的node放入另一個指標，再將指標指向linked list最後一個值
      > 若遇到重複值，只存取一次
        - 先判斷已存入的值是否與目標存入值相同
          - Yes：返回
          - No：使用while迴圈，如果下一個node存在，指標就往下一個node移動
            > 先判斷下一個node是否與目標存入值相同，是的話返回
         
            跳出while迴圈，指針指到linked list最後一個node，在指針的下一個創建新的node，存入目標值
            
- `remove`：刪除資料
  > 調整Runtime Error：目標不存在時
  >> - index已有值存在：調整移動指標的判斷
  >> - index未有值存在：直接跳出
  
   使用`Encoding_MD5`將要刪除的資料進行編碼
   - 如果目標刪除值所在的index是空的，返回
      > 目標刪除值不存在
   - 先判斷目標刪除值是否是array內的第一個node
      - Yes：是否有下一個node存在
        - Yes：將下一個node重新存入array中
        - No：將array內的值改為None
      - No：將指標指到目標刪除值，使用while迴圈移動指針，如果指標值與目標刪除值不同且指標值的下一個node存在，就往下一個移動
        > 因刪除會重新建立連結，所以也記錄指標的前一個node
        
        跳出while迴圈，若指針指到目標刪除值，就重新建立連結
        
- `contains`：包含、搜尋，是否存在此資料
  
  使用`Encoding_MD5`將要搜尋的資料進行編碼
  - 建立指標，使用while迴圈，若指標值與目標搜尋值不同，就往下一個node移動
    - 如果指標值與目標搜尋值相同，回傳True
    - 若搜尋到最後一個皆無找到相同，回傳False

# Demo
- add
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_12/image/1575385042454.jpg)
- remove
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_12/image/1575385083737.jpg)
- contains
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_12/image/1575385110448.jpg)
