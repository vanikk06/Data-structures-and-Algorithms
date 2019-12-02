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
  - array內儲存的是input，index由MD5決定


# Error

### TypeError
 > `missing 1 required positional argument`
 
在使用class建立物件時，使用class名稱，後面必定要帶**()**

#### Source
[問題Missing 1 required positional argument引出的關於python例項化的經驗教訓](https://www.itread01.com/content/1544325485.html)
