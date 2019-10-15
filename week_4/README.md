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


# Test Insertion  Sort List
> Following teacher's

[👉🏻HERE👈🏻](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/Test%20Insertion%20sort%20list.py)

Status：Runtime 276 ms, Memory 15.4 MB

#### Code

#### Wrong Answer
 - `it`指標是有別於`out`跟`tail`的第三個方法，在執行它時要將其他兩種的狀況排除
 ![wrong answer](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/image/1571141402660.jpg)
#### Runtime Error
 > 執行期錯誤，通常是跑到外面
 
 - `'NoneType' object has no attribute 'next'` 
![runtime error](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/image/1571141648113.jpg)


