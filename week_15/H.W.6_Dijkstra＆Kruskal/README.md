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


 - ⭐assignment⭐
    > 指派、賦值
   
   在python中`=`代表的是一個指派、賦值的動作，讓變數在記憶體中定址\
   當執行兩個變數相互指派的程式碼時，代表的是讓**兩個變數定址在相同的記憶體位置**
   ```python 
   a = [3]
   b = []
   
   b = a
   b.append(7)
   
   print('a = ', a)
   print('b = ', b)
   print( a is b )
   ```
   因為是在相同的記憶體位置，因此對其中一個變數作出變動時，會直接影響到另一個變數
   ```python
   a =  [3, 7]
   b =  [3, 7]
   True
   ```
   如果想要將a變數的值儲存到b變數內，但不想讓對b變動的變動影響到a變數的話，可以使用`.copy()`函式
    ```python 
   a = [3]
   c = []
   
   c = a.copy()
   c.append(8)
   
   print('a = ', a)
   print('c = ', c)
   print( a is c )
   ```
   結果
   ```python
   a =  [3, 7]
   c =  [3, 7, 8]
   False
   ```

# Code

使用`collections.defaultdict`套件

- `__init__`：基本屬性
    - .V：vertex個數
    - .graph：Dijkstra使用之adjacency matrix
        > 各個vertex之間的cost
        >> 0：未連結
    - .graph1：Kruskal使用之字典，資料類型為`defaultdict`，參數為int
    - .graph_matrix：Dijkstra使用之紀錄已檢查過的cost的矩陣
        >必為V x V矩陣
        >> 預設值為-1

- `addEdge`：建立edge，有三個參數
    - u：src，起點
    - v：dest，終點
    - w：weight/cost，權重、成本
    
        將edge加入graph1的字典中\
        - key：src - dest
        - value：weight/cost
    
- `Dijkstra`：最短路徑
    > 有一個參數：起點
    - s：起點/上一個找到最小路徑的vertex
    - min_cost：最小cost，每新增一個vertex就會變動
        > 以此去尋找相對應的index（vertex）
    - min_index：此次最小cost的index，也就是下次要增加的vertex
    - fix_min_index：修復index，排除bug
        > 當cost出現相同值時，因尋找index的方式是採用`list.index()`，它會回傳第一個相符值的index
    - fix_time：修復次數
        > 原始list中的index = fix_min_index + fix_time
        >> 因修復方法為「刪除第一個相符值」讓`list.index()`找到此次應增加的vertex\
        因刪除會使index產生變動，且第一個相符值必定存在於第二個相符值的前面\
        因此，將「修復次數」加上「修復後找到的index」即可得出原始正確的index
    - checked：紀錄已找到最小cost的vertex
    
    先設定一些小工具（min_cost、fix_min_index、fix_time、checked），方便等一下操作
    
    將起點連結到的vertex紀錄到graph_matrix上\
    使用`for`迴圈，一個個查看起點在graph中與其他vertex的連結情況
    > 將自己與自己的cost紀錄為0
    - 判斷vertex與起點是否有連結：
        - Yes：將graph上的cost紀錄到graph_matrix
            > 要找出此次最小的cost，以決定下次要增加的vertex為何                
            - 如果min_cost不存在：將min_cost存入此次cost
            - 如果此次cost小於min_cost：將min_cost存入此次cost
        - No：不執行任何動作
        
    建立起點的cost後，要一個個新增下一個vertex直到起點到所有vertex的最短路徑都找出
    > vertex：
    > - 直接與起點相連：直接紀錄cost
    > - 非直接與起點相連：透過已找出最小cost的vertex，間接找出走訪到其的最小cost
    
    使用`while`迴圈，尋找尚未找出最短路徑的vertex
    - 判斷checked長度是否等於vertex個數：
        - No：進入迴圈
        
          先透過min_cost找出下一個要尋找最短路徑的vertex，將尋找對象存入min_index
            - 檢查min_index是否已經存在於checked：
                - Yes：代表min_cost出現相同的值，需要修復min_index
                    - 如果fix_min_index不存在：將上一個vertex的cost紀錄複製到fix_min_index
                 
                    將fix_min_index中第一個符合min_cost的vertex移除\
                    找出下一個符合min_cost的vertex             
                - No：往下繼續執行
          將此次要尋找最短路徑的vertex加入checked裡面\
          先複製前一個vertex的cost紀錄到min_index的cost紀錄，再使用`for`迴圈一個個檢查增加min_index對每個vertex的最短路徑是否有要更新
            - 一個個查看min_index與每個vertex之間的關係
                - 已經存在在checked裡面：跳過，執行下一個
                   > 存在：已找出最短路徑
                 - vertex是否與min_index有連結：
                     - Yes：需要進一步判斷，此連結對原本的cost紀錄造成何種影響
                        > 會有兩種情形
                        - 原本與起點沒連結，但因min_index所以產生連結：此vertex的cost，為「起點到min_index的cost」加上「min_index到vertex的cost」
                        - 原本與起點已有連結，但因min_index所以產生新的連結選項：
                           - 判斷vertex新的連結方式的cost是否小於原本的cost
                              - Yes：更新cost
                                  > 新cost為「起點到min_index的cost」加上「min_index到vertex的cost」
                              - No：保持原本cost
                        
                     - No：執行下一個
          
            更新完增加min_index對起點到vertex的cost產生的變化後，要再從中找出這次最小的cost
            - 如果還沒找出所有vertex的最短路徑：
            
                創立一個temp變數，資料類型為list
                - 一個個對vertex進行判斷
                    - 將未找出最短路徑vertex的cost放入temp中
                        > 不存在在checked裡面
                        >> 有兩種情形：
                        >> 1. 已與起點建立連結，但還未找到最短路徑
                        >> 2. 未與起點建立連結
                找出temp中的最小值
             
             將這次處理完的min_index存入s中
             > s：上一個找到最小路徑的vertex  
                        
                    
        - Yes：跳出迴圈
        
    建立一個空的字典，命名為SP\
    一個個將vertex與起點到其的最短路徑轉換成字典格式\
    回傳SP
    
- `Kruskal`：最小生成樹
   - sort_graph：依weight/cost大小排序的list
      > data為(key, value)
   - src：起點list，index是按照sort_graph大小順序的edge
   - dest：終點list，index是按照sort_graph大小順序的edge
      > src[0]與dest[0]是weight/cost最小之edge的起點與終點
   - root：disjoint sets，資料類型為list，index為vertex，data為vertex之root
      > 預設值為-1
      >> 相同root代表vertex為相同的集合
   - edge：紀錄要採用的edge，data為對應sort_graph的index
   - j：int，排序後第j條edge，輔助走訪src與dest
      > 從0開始，最大值為edge個數

   利用`addEge(u,v,w)`建立vertex之間的連結，並依照graph1中value的大小，由小到大重新排序
   
   - 判斷edge的個數是否滿足vertex-1:
        - No：返回
            > edge不足無法形成spanning tree
            >> vertex並非完全連通
        - Yes：往下繼續執行
    
   建立src與dest變數，拆解已排序的sort_graph，按照edge由小到大的順序，依序加入edge的起點與終點
   
   建立root變數，其長度與vertex個數相同\
   建立一個空的list名為edge，並創立一個變數j
   
   使用`while`迴圈，操作root變數，一個個判斷edge，若採用即放到edge變數中，直到edge變數中的edge可以走訪完所有的vertex
    > 判斷關鍵：
    > 1. 是否會產生cycle
        >> cycle情況：
        >> - 起點與終點已是相同的root
        >> - 起點已是終點的root
    > 2. 從任一vertex出發，是否可以走訪完所有vertex
   - edge變數是否可以滿足spanning tree的生成：
        - No：進入迴圈
            - 第j條edge的終點其root為預設值
                > 有兩種可能：
                > 1. 尚未變動過
                > 2. ❣其本身是root
                
               - 進一步判斷第j條edge的起點是否已存在root：
                   - Yes：將終點放置與起點相同的root
                      > ❣有可能終點已經是別的vertex的root
                      
                      檢查root變數中是否存在以此終點為root的情形\
                      若存在，依次將他們的root更改為與此起點相同的root
                      
                   - No：將終點的root設為起點
                      > ❣有可能終點已經是別的vertex的root
                      
                      檢查root變數中是否存在以此終點為root的情形\
                      若存在，依次將他們的root更改為此終點之起點
                將第j條edge，加入edge變數中
                
            - 第j條edge「終點的root已為其起點」或是「終點的root已為起點的root」
                - Yes：跳過此條edge，往下一條edge繼續執行
                    > 若加入此edge，會產生cycle
            - 非上述兩種情形
               > 兩個root合併
               >> 要將被合併的root，其root也改為合併的root
                - 判斷第j條edge的起點是否已存在root：
                    - Yes：
                       > 要先排除會出現cycle的edge
                       
                       先將root變數中，所有root與第j條edge終點之root相同的vertex，其root更改為第j條edge起點的root\
                       再將第j條edge終點之root的root也改為第j條edge起點的root\
                       
                       將第j條edge，加入edge變數中
                    - No：
                       > 要先排除會出現cycle的edge
                       先將第j條edge終點之root的root，改為第j條edge起點\
                       再將root變數中，所有root與第j條edge終點之root相同的vertex，其root更改為第j條edge起點
                       
                       將第j條edge，加入edge變數中
            改為第j+1條edge繼續執行
                
        - Yes：跳出迴圈
        

