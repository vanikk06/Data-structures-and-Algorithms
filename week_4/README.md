# H.W._Quick Sort
[🤜HERE🤛](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4/H.W.)

  - [Jupyter notebook](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/H.W./H.W._Quick%20Sort%20(1).ipynb) 
  - [Jupyter nbviewer](https://nbviewer.jupyter.org/github/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/H.W./H.W._Quick%20Sort%20%281%29.ipynb)
    - [TypeError](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/H.W./README.md#typeerror)
  - [Demo](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/H.W./quick_sort_demo.jpg)
  - [Flowchart](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/H.W./quick_sort_flowchart_.jpg)

# Content
- [Sorting algorithms](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/README.md#sorting-algorithms)
- [Time complexity](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#time-complexity)
- [return VS. break VS. continue](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#return-vs-break-vs-continue)
- [not](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#not)
- [Ipynb change](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#ipynb-change)
- [Class notes](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#class-notes)
- [Insertion Sort ](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#insertion-sort)
    - [Test Insertion sort list](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#test-insertion-sort-list)
        - [Code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#code)
        - [Wrong Answer](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#wrong-answer)
        - [Runtime Error](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#runtime-error)
    - [Try Insertion sort list](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#try-insertion-sort-list)
- [Quick Sort](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/README.md#quick-sort)
     - [Extra-place](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/README.md#extra-place)
     - [Divide and Conquer](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/README.md#divide-and-conquer)
# Sorting algorithms

- Insertion Sort：插入排序法
- Quick Sort：快速排序法
- Heap Sort：堆積排序法
- Merge Sort：合併排序法 / 歸併排序法


| Sorting Algorithm | Average Time | Best Time | Worst Time | Extra Space | Stability |
| --- | --- | --- | --- | --- | --- |
| **Insertion Sort** | O(n²) | O(n) | O(n²) | O(1) | Stable |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(n) | Unstable |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | Unstable |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Stable |

#### Source
[Sorting algorithms](https://www.c-programming-simple-steps.com/sorting-algorithms.html)

[Time Complexities of all Sorting Algorithms](https://www.geeksforgeeks.org/time-complexities-of-all-sorting-algorithms/)

[Comparison Sort系列文章](http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html#series)

[Algorithm time complexity演算法時間複雜度整理](https://tingtseng.pixnet.net/blog/post/39924871-algorithm-time-complexity-%E6%BC%94%E7%AE%97%E6%B3%95%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%E6%95%B4%E7%90%86)

[15 Sorting Algorithms in 6 Minutes](https://www.youtube.com/watch?v=kPRA0W1kECg)


[🥜](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#content)

# Time complexity
The time complexity of an algorithm is an **approximation** of how long that algorithm will take to process some input.

> 時間複雜度：將事情拆解，計算出時間

- 演算法：將執行步驟具體寫成程式，用來達到特定目的的過程

  ` 輸入 + 演算法 = 輸出 `

評判演算法的好壞
> 是否有價值投入挑戰（鑑賞力）
  - 時間：速度有多快 → 時間複雜度
  - 空間：需要用到多少的記憶體

大O符號（Big O notation）
> 用來描述一個演算法在輸入n個東西時，總執行時間與n的關係（時間：以**步驟次數**而非以秒計）
>> 只要顯示佔據**領導**地位者(最高次方)，其他項即係數皆可省略

通常希望演算法至少能比 O(n²) 快，如果能達到 O(n)、O(1) 甚至是 O(log n) 的話是最理想的情況

> ↓ 隨者n增大，O(n²) 會大過O(2<sup>n</sup>)

![O](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/image/1571638832242.jpg)


- O(1)：**constant time**，無論input大小為何，運行所花費的時間都相同
- O(n)：隨著input個數(n)的增加，時間隨著n倍數成長

  > 逐筆跑完每筆資料
  ![O(n)](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/image/1571648550712.jpg)
- O(log n)：`log`降低input每個步驟執行的時間
  
  > 執行步驟逐漸減半
  ![O(log n)](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/image/1571648965575.jpg)
- O(n log n)：**divide-and-conquer**，描述資料結構每次運行要花費O(log n)時間

### Why是"步驟數"而不是"執行時間"

`演算法有多快不是以秒衡量，而是以步驟次數衡量`

因為電腦效能和語言特性都會對程式運行速度造成影響，因此使用"執行時間"來衡量演算法的快慢並不是個穩定的指標

#### Source
Class's PPT

[初學者學演算法｜談什麼是演算法和時間複雜度](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E8%AB%87%E4%BB%80%E9%BA%BC%E6%98%AF%E6%BC%94%E7%AE%97%E6%B3%95%E5%92%8C%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6-b1f6908e4b80)

[維基百科_大O符號](https://zh.wikipedia.org/zh-hk/%E5%A4%A7O%E7%AC%A6%E5%8F%B7#%E5%B8%B8%E7%94%A8%E7%9A%84%E5%87%BD%E6%95%B0%E9%98%B6)

[★ A coffee-break introduction to time complexity of algorithms ★](https://dev.to/victoria/a-coffee-break-introduction-to-time-complexity-of-algorithms-160m)

[🍅](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#content)

# return VS. break VS. continue
- `return`：直接**返回函式**，所有該函式內的程式碼都不會再執行
- `break`：跳出**當前所在的整個迴圈**，到外層程式碼繼續執行（跳出整個while或for）
- `continue`：跳出**本次迴圈**，從下一個迭代繼續執行迴圈

#### Source
[Python的return、break、continue區別](https://www.itread01.com/content/1548181641.html)

[🍆](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#content)

# not
>　邏輯運算符（and、or、not）
- !=：比較運算符（a與b之間關係）

#### Source
[Python 運算符](https://www.runoob.com/python/python-operators.html)

[🌽](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#content)

# Ipynb change
> github上jupyter notebook加載很慢，有時候加載不出來

[jupyter nbviewer](https://nbviewer.jupyter.org/)  ← 把github上對應文件的url輸進去

[🌶](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#content)

# Class notes
 
 - Why debug?：不知道有多少邏輯跟測資必須被歸納
   > Demo(步驟)、Flowchart(流程圖)
 - 程式
    1. 可以compile
    2. 可以答對 
    3. 時間最少，並且可以證明
 
[🍄](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#content)

# Insertion Sort
> 直觀的排序方法，一個個比較，小的就往前面插入

|| Average Time | Best Time | Worst Time | Extra Space | Stability |
| --- | --- | --- | --- | --- | --- |
|**Insertion Sort**| O(n²) | O(n) | O(n²) | O(1) | Stable| 

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

[[演算法] 插入排序法(Insertion Sort)_Demo](http://notepad.yehyeh.net/Content/Algorithm/Sort/Insertion/1.php)

[Insertion sort_](https://www.c-programming-simple-steps.com/insertion-sort.html)

[🥑](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#content)

## Test Insertion sort list
> Following teacher's → LeetCode：147. Insertion Sort List
>> Using linked list

[👉🏻HERE👈🏻](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/Test%20Insertion%20sort%20list.py)

Status：Runtime 276 ms, Memory 15.4 MB

使用linked list建立insertion sort，不需佔用太多記憶體空間（改變`next`連結就好）
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

[🥒](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#content)

## Try Insertion sort list
> By myself → LeetCode：147. Insertion Sort List
>> Using linked list

- 插入方式：利用`.next`重新建立連結

[🥒🥒](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#content)


# Quick Sort
> 利用Divide and conquer(分治法)，找一個基準點，根據基準點去作區分

|| Average Time | Best Time | Worst Time | Extra Space | Stability |
| --- | --- | --- | --- | --- | --- |
|**Quick Sort**| O(n log n) | O(n log n) | O(n²) | O(n) | Unstable| 

以**固定的方式**尋找基準點，依據基準點將元素分為三堆（extra-place）或兩半(in-place)，遞迴式重複此動作，直到無法執行，再將結果合併輸出

#### Source
[QuickSort](https://github.com/Alex-CHUN-YU/SortingAlogorithm/wiki/QuickSort)

[快速排序法(Quick Sort)](https://emn178.pixnet.net/blog/post/88613503-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95(quick-sort))

[3分鐘搞懂, 泡沫排序法vs快速排序法! | Bubble Sort vs Quick Sort](https://youtu.be/G4dwRF_Rzd0)

[Comparison Sort: Quick Sort(快速排序法)](http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html)

#### Others
[How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/?fbclid=IwAR1olxlNcAQhKZVNw6-JBCituCKsqfk3YL67xOMfQA-_fyqbHyrFJRm15T4)

[🥦](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#content)


## Extra-place
>  Following blog
>> Using list

[👉🏽HERE👈🏽](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/Quick%20sort_Extra%20place.py)

以第一個數為`key`，將其作為基準點與list內的每個元素比較，以此分為三堆`> key`、`= key`、`< key`，再以`< key` + `= key` + `> key`合併，不斷地對`< key`與`> key`重複此行為，直到無法執行將結果輸出
  
  - [TypeError](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4/H.W.#typeerror)
  - [Demo](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4/H.W.#quick-sort-demo)
  - [Flowchart](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4/H.W.#quick-sort-flowchart)
 
 #### Source
 [[ 資料結構 ] 快速排序法（Quick sort）in Python](http://jialin128.pixnet.net/blog/post/142927691-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88quick-sort%EF%BC%89in-python)

[🥦🥦](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#content)

## In-place
>  Following blog
>> Using list

[👉🏽HERE👈🏽](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/Quick%20sort_In%20place.py)

不使用額外空間的Quick sort的邏輯，像是從目標結果回推
- 目標：`小於_基準點` + `基準點` + `大於_基準點`

為達上述的元素排列，從兩邊（左邊(頭)、右邊(尾)）向中間走，在兩者相遇之前，找出不符合的(下述)，將兩者交換
  - 左邊(頭)：大於_基準點
  - 右邊(尾)：小於_基準點

如此跑完元素會分為兩半，左邊走過的是`小於_基準點`，右邊走過的是`大於_基準點`，再將`基準點`放置兩者中間，遞迴式的對`小於_基準點`與`大於_基準點`重複執行此動作，直到元素皆完成排序
  
#### Code
  > 由於input為list，所以從左邊、右邊進行走訪會需要index值（長度）
  
  使用兩層`def`，先將Quick sort的執行運作寫出，再利用另一個函式呼叫並帶入input的index值
  - 先判輸入的index是否有誤
    > left：頭 ; right：尾
  - 將第一個值設為key，並將頭尾的index存到另一個變數(left_point、right_point)中，方便等下走訪
  - 在滿足左邊index小於右邊index的情況下，開始進行走訪
      1. 先從右邊往左邊走
        > 是否 左邊index小於右邊index 且 值 >= key
          - Yes：繼續往下一個走
          - No：將right_point指在那個位置
      2. 再從左邊往右邊走
        > 是否 左邊index小於右邊index 且 值小 <= key
          - Yes：繼續往下一個走
          - No：將left_point指在那個位置
      3. 確定是否right_point > left_point
          - Yes：將兩個值互換位置
          - No：不執行
  

#### Q&A
  1. 找出兩邊不符合的部分，再將兩者交換。若一邊無不符合部分，一邊有時，怎麼辦？
  2. 在兩邊交會時，該由誰與key交換？
      

#### Demo
  > 與Extra-place相同例子


#### Source
 [[ 資料結構 ] 快速排序法（Quick sort）in Python](http://jialin128.pixnet.net/blog/post/142927691-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88quick-sort%EF%BC%89in-python)

[🥦🥦🥦](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#content)

## Divide and Conquer
> 分而治之，**遞迴**的典型應用

- 分為三個階段：
    - Divide（分割）：將大問題不斷切割成兩個或多個小問題
    - Conquer（克服）：透過小問題的解決，一步步向上**堆疊**，最後解決原本的大問題
- 優點
    a. 將困難的問題簡化為容易實作的方式
    b. 能夠平行處理，提升程式效率
    
#### Source
[分治演算法（divide and conquer）](https://www.itread01.com/content/1547872030.html)

[Divide and conquer_範例](https://emn178.pixnet.net/blog/post/87739443-divide-and-conquer)

[🥦🥦🥦🥦](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_4#content)
