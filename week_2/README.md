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
      
      `Class的概念是**屬性集合**，不是所有物`  (屬性是self本身蘊含的性質、特性) 
   
 >兩個__init__概念:
  - 設定可以有些變化
      - 先給一個預設值：第一次呼叫就不用給屬性  (如果是固定值可以直接設定)
      - 也可以是空的，之後再新增資料
  - 並不是必要的
  
       python自由度高，可以直接給屬性，不透過`__init__`


 #### Source
[Python Class](https://medium.com/@weilihmen/%E9%97%9C%E6%96%BCpython%E7%9A%84%E9%A1%9E%E5%88%A5-class-%E5%9F%BA%E6%9C%AC%E7%AF%87-5468812c58f2)

[🛸](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_2#content)



# return
> keyword用在函數或方法中**回傳值(return value)**，若在函數或方法中沒有用到return，**預設回傳None**
  - 基本上，只會回傳一個數值，若逗號區隔多個數值，則回傳一個序對(tuple)
  - 若出現在函數或方法外，會錯誤
    > P.S. 函式或方法中回傳較不適用`print()`，print是打印，放到def中，執行到會打印出設定的結果，但此並非def的回傳值，所以仍會回傳預設的return(None)
    
 ![image](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_2/image/1570076731275.jpg)
    
#### Source
[Python 簡單陳述return](https://kaiching.org/pydoing/py/python-return.html)

[🚈](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_2#content)

# Design Linked List
> Array VS. Linked list
 - Array
    - pros:
        1. 連續的記憶體空間
        2. 速度快，放入資料是連續的(走訪方便)
    - cons:
        連續的記憶空間，無法有效使用記憶體(零星的空間)
 - Linked list
      - pros:將空間中零碎的空間串起，優化記憶體配置
      - cons:資料不連續，要建立空間的連結
      
 #### Blockchain 區塊鏈
 > 分散式架構的資料運算與儲存平台，同時具備特殊的P2P(點對點)特性
  - 特性；
      1. 去中心化
      2. 不可竄改之安全性
 
`linked list中再包一個hash`
  - hash
      - One way:無法往回影響(不被串改)
 
#### Source
[區塊鏈是什麼?](https://medium.com/cobinhood-%E4%B8%AD%E6%96%87%E5%A0%B1/what-is-blockchain-53a7ee374e6c#8f35)


[白話的Hash Table](https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/)

[🛫](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_2#content)
   


## Test linked list
> following teacher's
由`node`跟`pointer`組成
  - `node`:創造儲存值的空間
  - `pointer`:將空間與空間組合起來，串起零碎的空間
