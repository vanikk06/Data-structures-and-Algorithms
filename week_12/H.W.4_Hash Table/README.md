# H.W.4_Hash Table notes
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

# Code
  > 使用兩個class，一個MD5套件

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
  - .data：在特定的array[index]內儲存的資料
  
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
  
   使用`Encoding_MD5`將要增加的資料進行編碼
   - 先判斷目標刪除值是否是array內的第一個node
      - Yes：是否有下一個node存在
        - Yes：將下一個node重新存入array中
        - No：將array內的值改為None
      - No：將指標指到目標刪除值，使用while迴圈移動指針，如果指標值與目標刪除值不同，就往下一個移動
        > 因刪除會重新建立連結，所以也記錄指標的前一個node
        
        跳出while迴圈，指針指到目標刪除值，重新建立連結
