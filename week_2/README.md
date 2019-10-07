# Content
  - [Class](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_2/README.md#class)
  - [return](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_2/README.md#return)
  - [Design Linked List](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_2/README.md#design-linked-list)
    - [Test linked list](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_2/README.md#test-linked-list)


# Class
  > 像是一個模組，產出具有相同特性的實體(物件)
   - `class` 跟 `def` 是組成模組功能的最低架構
   - 定義一個類別名稱
      
 `def__init__(self)`宣告class的"起手式"
   - 宣告時會自動執行
   - 一般拿來放基礎的屬性設定
      - `self`是class本身，在第一個不用變動
      - 在創造時，必須要給屬性一個參數，才能成功創造
      
      `Class的概念是"屬性集合"，不是所有物`  (屬性是self本身蘊含的性質、特性) 
   
 >兩個__init__概念：
  - 設定可以有些變化
      - 先給一個預設值：第一次呼叫就不用給屬性  (如果是固定值可以直接設定)
      - 也可以是空的，之後再新增資料
  - 並不是必要的
  
       python自由度高，可以直接給屬性，不透過`__init__`


 #### Source
[Python Class](https://medium.com/@weilihmen/%E9%97%9C%E6%96%BCpython%E7%9A%84%E9%A1%9E%E5%88%A5-class-%E5%9F%BA%E6%9C%AC%E7%AF%87-5468812c58f2)

[🚗_](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_2#content)



# return
> keyword用在函數或方法中**回傳值(return value)**

> 若在函數或方法中沒有用到return，**預設回傳None**

> 若在函數或方法中放入`return`加**空值**，會跳出函數或方法
  - 基本上，只會回傳一個數值，若逗號區隔多個數值，則回傳一個序對(tuple)
  - 在Class內編輯函數或方法時，若無return(讓函數或方法跳出)，小心計算超時
  - 若出現在函數或方法外，會錯誤
    > P.S. 函式或方法中回傳較不適用`print()`，print是打印(裡面不能放運算式)，放到def中，執行到會打印出設定的結果，但此並非def的回傳值，所以仍會回傳預設的return(None)
    
 ![image](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_2/image/1570208923463.jpg)
    
#### Source
[Python 簡單陳述return](https://kaiching.org/pydoing/py/python-return.html)

[🚕__](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_2#content)

# Design Linked List
> Array VS. Linked list
 - Array
    - pros：
        1. 連續的記憶體空間
        2. 速度快，放入資料是連續的(走訪方便)
    - cons：
        連續的記憶空間，無法有效使用記憶體(零星的空間)
 - Linked list
      - pros：
        1. 不需使用連續記憶體空間，不需事先指定串列大小
        2. 將空間中零碎的空間串起，優化記憶體配置
      - cons：
        1. 資料不連續，要建立空間的連結(走訪必須一個個走訪)
        2. 使用額外的記憶體空間紀錄node指標
      
 #### Blockchain 區塊鏈
 > 分散式架構的資料運算與儲存平台，同時具備特殊的P2P(點對點)特性
  - 特性：
      1. 去中心化
      2. 不可竄改之安全性
 
`linked list中再包一個hash`
  - hash
      - One way：無法往回影響(不被串改)
 
#### Source
[區塊鏈是什麼?](https://medium.com/cobinhood-%E4%B8%AD%E6%96%87%E5%A0%B1/what-is-blockchain-53a7ee374e6c#8f35)


[白話的Hash Table](https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/)

[🚙___](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_2#content)
   


## Test linked list
[👉🏻HERE👈🏻](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_2/Test%20%20design%20linked%20list.py)
> following teacher's

由`node`跟`pointer`組成一連串的linked list
  - `node`：創造儲存值的空間
  - `pointer`：將空間與空間組合起來，串起零碎的空間

Code
- `__init__`:node基礎的屬性設定
  - .val：node內儲存的值
  - .next：node和下一個node之間的連結(pointer)
- `get(index)`：得到node在linked list中的index，如果index無效，回傳-1
    > 考慮index位置，起初，箭頭指在第一個node的位置，往後必須一個一個走訪
    - 要第一個位置的值
        > 第一個的值是否已經存在!?
        - 存在：回傳箭頭所在位置的值
        - 不存在(空值)：回傳-1
    - 要第一個以後的值：一個個往下指到index的位置
        >下一個是否存在!?
        - 存在：箭頭指向下一個，指到index回傳值
        - 不存在：回傳-1
- `addAtHead(val)`：增加一個值是val的node在所有node的前面，第一個(向左增加)
    > 考慮第一個node是否已經有值存在
    - 存在：將原本的值存到一個暫存的空間，把val存入空出來的位置，再在他的下一個創造一個新的node空間，存入原本的值，並把原本值的下一個指派給val的下下一個
    - 不存在(空的)：直接存到第一個node中
- `addAtTail(val)`：增加一個值是val的node在所有node的後面，最後一個
    > 考慮前面是否已經存在
    - 存在：箭頭指到最後一個，在它之後創要一個node空間，存入val
    - 不存在：直接存到第一個node中
- `addAtIndex(index, val)`：增加一個值為val的node在指定的index位置
    > 先考慮位置，再考慮插入的方法
    - index <= 0：向左增加，使用`addAtHead()`向前插入
    - index > 0：向右增加，先指到index位置
        > index是否在linked list的長度內?!
        >> 走訪在乎是否走到index或是最後一個，而非下一個是否存在(先走再判斷)
        - Yes：將箭頭指到index位置 
            (往下條件：self != None and self.val != None，前者判斷是否為最後一個，後者避免linked list建構失敗)
        - No：指到最後一個
          > 插入方法：把箭頭指到index，在那個位置插入一個新的node (在*index-1的下一個位置*創造一個node)
- `deleteAtIndex(index)`：刪掉在index上的node
    > 考慮位置、是否為空值
    - index < 0：不存在，return
    - index == 0：刪掉第一個
        > 第一個是否為空值?!
        - Yes：return
        - No：
            > 後面是否有node?!
            - Yes：改變node的連結，將第二個node取代第一個node
            - No：將self設為空值，return
    - index > 0：
        > index是否大於linked list的長度
        - Yes：最後一個後面.next = None
             (往下條件：`pre != None`，)
        - No：重新建構連結，讓index-1的下一個和index的下一個建立連結
    

Wrong Answer
  1. 在函式中`return`後面加**空值**時，會直接跳出函式
  ![Return](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_2/image/Return.jpg)
  2. p = self，`p = p.next`才是建立node的連結
  ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_2/image/addAtTail.jpg)

[🚌____](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_2#content)
