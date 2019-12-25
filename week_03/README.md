# Content
- [Object](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#object)
- [Array VS. List VS. Linked list](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#array-vs-list-vs-linked-list)
- [Python list vs. array](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#python-list-vs-array)
- [List](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#list)
- [Stack & Queue](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#stack--queue)
    - [Try Min stack ](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#try-min-stack)
        - [Code_by linked list](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#code)
        - [Code_by list](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#code-1)
            - [Note](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#note)
    - [Test Min stack](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#test-min-stack)
        - [Code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#code-2)
    - [Try Implement queue using stacks](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#try-implement-queue-using-stacks)
        - [Code_by linked list](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#code-3)
        - [Code_by list](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#code-4)
    - [Test Implement queue using stacks](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#test-implement-queue-using-stacks)
        - [Code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#code-5)
    - [Try Implement stack using queues](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#try-implement-stack-using-queues)
- [Test Set mismatch](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#test-set-mismatch)
    



# Object
在Python中，所有的操作都是針對object(對象)，一個object包括兩方面的特徵：
> object(對象)=屬性+方法
 - 屬性（類別屬性class attribute）：描述它的特徵
 - 方法（實例屬性instance attribute/資料屬性data attribute）：它所具有的行為
    > 其實也是一種屬性，一種區別於數據屬性的可調整屬性
 
 把具有相同屬性和方法的object歸為一類，即為`class`，一種模型、藍圖，可創鍵多個object實例
 ```
 - class是object的抽象化，object是class的實例化。
 - class不代表具體的事物，object表示具體的事物
 ```
 
 在python中的`None`
  - 一種數據類型：表示該值是一個**空對象**，一種特殊的值，不可理解為0，因為0是有意義的，None是特殊的空值
  - 判斷時為False
  
  
  #### Source
 [Python對象](https://blog.csdn.net/Li_Danny/article/details/49815761)
 [淺談Python的屬性](https://marco79423.net/articles/%E6%B7%BA%E8%AB%87-python-%E7%9A%84%E5%B1%AC%E6%80%A7/)

[🐟](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#content)

# Array VS. List VS. Linked list 
> 資料結構是一種電腦運作的方法

在Python裡，同樣是陣列，但有array和list兩種數據類型
- array：屬於模組numpy裡的一種數據類型，所包含的**元素類型必須全部相同**
- list：屬於Python內建的數據類型，可以包含**不同的元素類型**
  > Why? 保存的資料是*數據存放的位置（指標）*，而非資料本身
- linked list(串列)：改變list中，讀取資料記憶體位置的順序
  > array在記憶體中的儲存空間是有連續性的，每一個位置都指向下一筆資料

#### Source
[陣列(Array) & 串列(Linked list)](https://ithelp.ithome.com.tw/articles/10203422)

[🐠~](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#content)

# Python list vs. array
  > 從「記憶體」角度

python雖然好用，但時常被詬病執行速度非常慢，numpy.array優化了python內建的list缺點

#### python與記憶體
當宣告一個變數`a=5`時，python會去跟電腦要一塊記憶體，將5存到這塊記憶體內，並在mapping table記下變數a與其記憶體位置

當呼叫a時，python就會到其記憶體位置內去抓取存在記憶體內的值

#### list vs. array
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_03/image/Snipaste_2019-12-26_02-26-17.png)

- list：內部儲存的是一堆pointer，因此除了儲存資料的記憶體之外，還需要一個額外的空間，來儲存pointer的對應位置
    > 其對應記憶體的位置
- array：直接將data存在裡面，跟電腦要一大塊連續且不能斷裂的記憶體，將資料儲存進去（不需要額外的空間儲存對應位置）
    > 較快，較省空間
    >> 快：內部data型態一致，不須一一比對
        

|  | list | array |
| --- | --- | --- |
| **記憶體** | 分散不連續，需要額外空間紀錄對應位置 | 連續不間斷 |
| **長度** | 可改變 | 不可變 |
| **內部資料型態** | 不拘 | 一致 |

#### Source
[用記憶體管理講解為何 python 的 list 那麼慢](https://medium.com/@t0915290092/%E7%94%A8%E8%A8%98%E6%86%B6%E9%AB%94%E7%AE%A1%E7%90%86%E8%AC%9B%E8%A7%A3%E7%82%BA%E4%BD%95-python-%E7%9A%84-list-%E9%82%A3%E9%BA%BC%E6%85%A2-bf2cd80bbf72)

[圖片來源](https://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/)

[🦐~~](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#content)

# List
list(列表)：偏向更簡單的struct
 > struct特性：可以放很多不同類型的型態進去
    
相關參數： 
- `list.append(x)`：將x元素增加到list尾端，等同`list[len(list)] = [x]`
- `list.extend(L)`：將L列表(list)增加到list尾端，等同`list[len(list)] = L`
> append全部加在最後一筆[-1]，extend從最後面一筆筆加上(拆開)
-`list.insert(i, x)`：將x元素插入第i個index位置
- `list.remove(x)`：刪除list中第一個x元素(遇到的第一筆)
- `list.pop(i)`：取出list中第i個元素，並將其刪除
- `list.pop()`：取出list最尾端的元素，並將其刪除
- `list.index(x)`：找出X元素的第一個index
- `list.count(x)`：X元素的數量
- `list.sort()`：由小到大排序
- `list.reverse()`：由大到小排序
- `list.copy()`：拷貝list
- `list.clear()`：清除list內所有資料

[🐡~~~](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#content)

#### Source
[list 參數](https://www.brilliantcode.net/713/python3-6-list-tuple-set-dictionary/)

# Stack & Queue
 > 儲存資料的方式
  - [Stack](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#stack)
  - [Queue](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#queue)
 
 ## Stack
  > 先進後出（LIFO：last in first out）
  
  ![stack](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_03/image/1571423793515.jpg)
  
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
    
  [~🦑](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#content)
 ## Queue
  > 後進先出（FIFO：first in first out）
  
  ![queue](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_03/image/1571424208826.jpg)
  
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
   
  [🐙~](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#content)
  
#### Source
 [Data Structures: Stacks and Queues](https://www.youtube.com/watch?v=wjI1WNcIntg)

## Try Min stack
> By myself → LeetCode：155. Min Stack
>>  Using linked list

[👉🏻HERE👈🏻](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_03/Try%20Min%20stack%20By%20linked%20list.py)

🚫Status：Time Limit Exceeded

- 利用`node`建立儲存空間（包含.val和.next），無增加min
- 箭頭指在top那筆資料

#### Code
- `__intit__`：min stack基礎的屬性設定
     - .topnode：ˋ在stack內top那筆資料
 - `push(x)`：增加一筆資料，變成新的top
   > 考慮stack內是否已有值存在
   - Yes：創建一個node存入x值，成為新的topnode，next為舊的topnode
   - No：創建一個node存入x值，成為topnode，next為None
 - `pop()`：取出top的資料，將下一筆資料成為新的top
 - `top()`：查看top那筆資料的值
 - `getMin()`：一筆筆比較stack中的值，找出最小值     🤺🤺🤺
   > 利用node.next比較各筆資料，不動到topnode的指標
   
> By myself → LeetCode：155. Min Stack
>> Using list

[👉🏼HERE👈🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_03/Try%20Min%20stack%20By%20list.py)

 Status：Runtime 72 ms, Memory 17.8 MB
 
 - 將top的資料，存在list最後一筆
 - 使用tuple的方式存入資料(x, min)
 
 #### Code
 - `__intit__`：min stack基礎的屬性設定
     - .min_stack：空的list
 - `push(x)`：增加一筆資料，變成新的top
   > 考慮stack內是否已有值存在
   - Yes：比較x與上一筆資料誰為min，以(x, min)方式增加
   - No：利用`append()`在list內增加一筆資料(x, x)
 - `pop()`：利用`pop()`回傳最後一筆資料，並將它刪除
 - `top()`：查看最後一筆資料第0的位置
 - `getMin()`：查看最後一筆資料第1的位置
 
 #### Note
  - 判斷list為空：空list本身等同於False，不可使用`!= None`，只要有object存在(不為空值)，`if list != None`就會為True
  ```Python
   list = []
   
   if list:           #Yes
        
   if list != None:   #No
  ```
  > None、0、0.0、""、()、{}本身都皆為False
  

 #### Source
 [Python 判斷list是否為空](https://www.itread01.com/p/435567.html)
 
[~~🦑](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#content)


## Test Min stack
> Following teacher's → LeetCode：155. Min Stack
>> Using linked list

[👉🏽HERE👈🏽](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_03/Test%20Min%20stack.py)

Status：Runtime 76 ms, Memory 18.6 MB


資料結構：先進後出，取出必須要是`top`的資料
 - 利用`node`建立儲存空間（包含.val和.next），多加一個.min，配合要求
 - 箭頭指在top那筆資料

#### Code
 - `__intit__`：min stack基礎的屬性設定
     - .topnode：在stack內top那筆資料
 - `push(x)`：增加一筆資料，變成新的top
   > 考慮stack內是否已有值存在
   - Yes：先將topnode.min存到暫存區，創建一個node存入x值成為topnode，再與暫存區內的值做比較
      - 小於：取代topnode.min
      - 大於、等於：不動
   - No：創建一個node存入x值，成為topnode
 - `pop()`：取出top的資料，將下一筆資料成為新的top
 - `top()`：查看top那筆資料的值
 - `getMin()`：查看stack中最小的值
    > 在node屬性中增加一個.min的屬性，在增加資料時，就將最小值的val當作屬性儲存
 
 ##### Source
 [用兩個stack來實作MinStack：O(1)](http://alrightchiu.github.io/SecondRound/stack-neng-gou-zai-o1qu-de-zui-xiao-zhi-de-minstack.html#minstack)
 
[~~~🦑](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#content)


# Try Implement queue using stacks
> By myself → LeetCode：232. Implement Queue using Stacks
>> Using linked list

[👉🏾HERE👈🏾](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_03/Try%20Implement%20queue%20using%20stacks%20By%20linked%20list.py)

#### Code


#### Source
[LeetCode-232-Implement Queue using Stacks](https://blog.csdn.net/yongwan5637/article/details/79251514)




> By myself → LeetCode：232. Implement Queue using Stacks
>> Using list

[👉🏿HERE👈🏿](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_03/Try%20Implement%20queue%20using%20stacks%20By%20list.py)

#### Code

[🐙~~](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#content)

 # Test Implement queue using stacks
 > Following teacher's：LeetCode：232. Implement Queue using Stacks
 >> Using array
 
 [👉HERE👈](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_03/Test%20Implement%20queue%20using%20stacks.py)

Status：Runtime 40 ms, Memory 13.7 MB

資料結構：
  - queue：先進先出
  - stack：先進後出
    
利用stack的方式建構queue，為了配合stack的結構，在取出資料或是查看資料時，不能直接取出要做些調整
    
#### Code
- `_init_`：利用**兩個stack**來進行調整
    - .stack_stack：直接使用stack結構，先進後出
    - .stack_queue：重新放入stack_stack，以此將其原本的結構方式改為queue
- `push`：放入資料，按照stack結構
- `pop`：取出資料並刪除，按照queue結構
    - 若stack_queue內有東西，直接取出並刪除
        > 在stack_queue內的資料放置方式，已符合queue的資料結構，所以直接執行即可
    - 若stack_queue內無東西，將stack_stack以stack方式取出，重新放到stack_queue內，再從stack_queue內將資料取出並刪除
- `peek`：查看第一筆資料，按照queue結構
    - 若stack_queue內有東西，直接回傳
        > 在stack_queue內的資料放置方式，已符合queue的資料結構，所以直接執行即可
    - 若stack_queue內無東西，將stack_stack以stack方式取出，重新放到stack_queue內，再從stack_queue回傳
- `empty`：裡面是否有資料
    - 若stack_stack與stack_queue內皆空的，回傳True



[🐙~~~](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#content)

# Try Implement stack using queues
> By myself → LeetCode：225. Implement Stack using Queues

#### Source
[[LeetCode]225. Implement Stack using Queues](https://www.itread01.com/content/1545554882.html)

[🦑🐙](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#content)

   
# Test Set mismatch
 > Following teacher's：LeetCode：645. Set Mismatch
 
 
[this](https://github.com/pecu/DSA/tree/master/03_Set)


[🐋](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_03#content)
