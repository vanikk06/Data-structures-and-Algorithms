[MD5套件](https://kite.com/python/examples/2084/crypto-generate-a-new-md5-hash)
  - 宣告物件時，要先`.new()`一個初始的
  - 塞物件`.update`：這物件裡面要開始轉換
    > 要告訴它編碼為何`.encode("utf-8")`，無此會Error
    
    > 轉出來16進位，要再轉為10進位(not正規)