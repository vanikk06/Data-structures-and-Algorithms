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
