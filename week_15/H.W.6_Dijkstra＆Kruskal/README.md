# Content

# Notes

- graph：有起點、終點、cost
- `addEdge`：新增edge，加上權重
    > idea：使用dict紀錄
    - u：起點
    - v：終點
    - w：權重
- 測資皆為正整數

Dijkstra先建一個權重的matrix（index由由0開始，為nxn矩陣）
  > 回傳值：input到每vertex的最短距離
  >> type dictionary

Kruskal建立edge不侷限用defaultdict
   > 回傳值：從最小的weight開始，起點-終點（小-大）

# Error

- TyprError
   > `unsupported operand type(s) for +: 'int' and 'str'`
   >> 類型錯誤：不支持操作類型為整數和字串
   
    `+`：符號操作，可分兩類
    - 數學運算符：在int、float等數字類型資料之間進行加法的操作
    - 字串連接：對str的資料類型進行連接的動作
    
    在`+`出現在**既有數字類型資料又有字串類型資料**的情況下，python會不知道是要進行數字運算還是字串連接的動作

#### Source
[Python初學者錯誤：TypeError: unsupported operand type(s) for +: 'int' and 'str'](https://blog.csdn.net/foryouslgme/article/details/51536882)
