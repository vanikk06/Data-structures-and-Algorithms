# return VS. break VS. continue
- `return`：直接**返回函式**，所有該函式內的程式碼都不會再執行
- `break`：跳出**當前所在的整個迴圈**，到外層程式碼繼續執行（跳出整個while或for）
- `continue`：跳出**本次迴圈**，從下一個迭代繼續執行迴圈

#### Source
[Python的return、break、continue區別](https://www.itread01.com/content/1548181641.html)

# not
>　邏輯運算符（and、or、not）
- !=：比較運算符（a與b之間關係）

#### Source
[Python 運算符](https://www.runoob.com/python/python-operators.html)


# Insertion Sort Algorithm
> 直觀的排序方法

- Algorithm：一種手段、過程或是一種方法
- Program：特定algorithm的具體實現，或可以成為某個algorithm的具體實現

依次檢查每個元素，將其與前一個元素比較，若其小於前一個元素，兩者互換位置
> 將資料分為以排序、未排序兩部份

- Code

![code](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/image/1571114698076.jpg)

 - Flowchart
 
![flowchart](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/image/1571081952907.jpg)


#### Source
[Insertion Sort Algorithm](https://www.junyiacademy.org/science/computer-science/v/insertion-sort-algorithm)


# Test Insertion sort list
> Following teacher's

[👉🏻HERE👈🏻](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/Test%20Insertion%20sort%20list.py)

Status：Runtime 276 ms, Memory 15.4 MB

使用linked list建立insertion sort
> 區分"已排序(out)"跟"未排序(head)"

#### Code
 - 首先判斷`head`是否存在，以及`head.next`是否存在
 - 將第一個值從head中移除
      - 創立一個`out`指標，指向最小的值
      - 創立一個`tail`指標，指向最大的值
        > `tail.next` = None（最後一個）
 - 一個個將未排序元素抽出與以排序元素比較
      - 是否比目前最小值`out`小
         - 取代為新的`out`
      - 是否比目前最大值`tail`大
         - 取代為新的`tail`
      - 介於`out`與`tail`中間
        > 創立一個新指標`it`，一個個往下指
         - `temp.val`是否大於`it.next.val`
             > 因為插入方式為改變next連結，所以拿`it.next.val`來判斷是否往下指
                   
              - Yes：往下一個指
              - No：插入
                 > 注意! `it`指標頂多指到`tail`的前一個
                 >> `it.next != tail`有無不影響compile

#### Wrong Answer
 - 若用`or`只有在兩者皆為False時才會跳出while迴圈，以此依定在`tail`的前一個插入
 ![wrong answer](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/image/1571141402660.jpg)
#### Runtime Error
 > 執行期錯誤，通常是跑到外面
 
 - `'NoneType' object has no attribute 'next'` 
![runtime error](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/image/1571141648113.jpg)


|OR|T|F| |AND|T|F|
| --- | --- | --- | --- | --- | --- | --- |
|**T**|T|T| |**T**|T|F|
|**F**|T|F| |**F**|F|F|

# Try Insertion sort list
> By myself

- 插入方式：利用`.next`重新建立連結
