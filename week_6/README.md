# Content
 - [Sorting algorithm stability](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#sorting-algorithm-stability)
 - [range](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#range)
 - [Division differences](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_6/README.md#division-differences)
 - [Heap Sort](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#heap-sort)
    - [Test Design heap sort](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#test-design-heap-sort)
       - [Code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#code)
    - [Try Design heap sort](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#try-design-heap-sort)
       - [Code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#code-1)
 - [Test Univalued Binary Tree](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#test-univalued-binary-tree)
 - [Try Univalued Binary Tree](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#try-univalued-binary-tree)

# Sorting algorithm stability
如果在一個待排序的序列中，存在2個相等的數，在排序後這2個數的相對位置保持不變，那麼該排序演算法是穩定的；否則是不穩定的。

> 穩定性的意義
  - 交換元素存在一定的開銷，若是穩定的，元素交換的次數可能會減少

如下述的例子，當我們對第一個數進行排序後，可能會需要對第二個數進行排序，若在第一次排序時不改變第一個元素相同的值的相對位置，第二次排序就可以減少交換的次數  e.g.[基數排序](https://www.cnblogs.com/sun/archive/2008/06/26/1230095.html)

###### Example
```
(4,1), (3,1), (3,7), (5,6) 使用第一個數進行排序
```
再經過排序之後
```
(3,1), (3,7), (4,1), (5,6) → 穩定性
(3,7), (3,1), (4,1), (5,6) → 不穩定性
```



#### Source
[判斷各種排序演算法的穩定性](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/548443/)

[排序演算法的穩定性](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/92550/)

[維基百科](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95#%E7%A9%A9%E5%AE%9A%E6%80%A7)

[🍕](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#content)

# range
```python
range(start, stop, step)
```

 - start：開始，計數從start開始
      > 默認是從0開始 e.g.range(5) == range(0, 5)
      >> range(5)：從0開始到5
 - stop：結束，計數到stop結束，但是**不包括stop**
      > e.g.range(0, 5)：[0,1,2,3,4]，沒有5
 - step：間隔，默認值為1

#### Source
[python 3 range用法](https://www.itread01.com/content/1525936808.html)

[🥞](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#content)

# Division differences
> 除法差異

- //：取商數，運算之後取**最小整數**
  > 當商數為負數時，會error
 
 ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_6/image/1572943931909.jpg)
  
- int()：取整數，小數點後的數**全部捨去**

 ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_6/image/1572944683672.jpg)
 
[🧀](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#content)


#  Heap Sort
> tree's special case

linked list的變形，每一個node都有且僅有**兩個subnode**，放置順序必為**先左後右**，所有值排完之後，剩下空缺值皆集中在右下方

  > 根據roof值的大小作區分
  
  ![heap sort](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_6/image/1571665085656.jpg)

- Heap Sort：將數列使用Heap結構存入後依序取出的結果
    > 必定為有排序的
     - 由小到大：Min heap
    - 由大到小：Max heap

- time complexity：穩定的 O(n log n)
   > 有n個值，每個值都要rebalance出一棵樹(O(log n))
   
| | Average Time | Best Time | Worst Time | Extra Space | Stability |
| --- | --- | --- | --- | --- | --- |
|**Heap Sort**| O(n log n) | O(n log n) | O(n log n) | O(1) | Unstable |
> Why heap sort is unstable
>> 因為把資料重新放入一個Binary tree(二叉樹)的結構

- tree資料結構：快速排序、快速搜尋
  > e.g.資料庫：資料存取模式

#### Binary tree
生成node：由上往下、由左往右

#### Debug Mode
> Spyder

帶測值進去跑，看它如何運作
- check point：設在細節不理解之處

#### Source
[Heap Data Structure](https://www.geeksforgeeks.org/heap-data-structure/)

[Heap Sort: how to sort?](https://stackoverflow.com/questions/13979714/heap-sort-how-to-sort)

#### Others
[我以為的軟體工程師九層分級架構](https://ascii-iicsa.blogspot.com/2010/11/blog-post.html)

[推薦書](https://www.books.com.tw/products/0010771263)

[🍔](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#content)

# Test Design heap sort
> Following Teacher's
>> Using array：Max heap

[👉🏽HERE👈🏽](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_6/Test%20Design%20heap%20sort_bug.py) ← has bug

[👉🏼HERE👈🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_6/Test%20Design%20heap%20sort_debug.py) ← debug，課堂範例Code

🐛Status：has bug
   > 若最大值存在root的sub-subnode內，因無回頭check，會出現bug
   >> e.g.[4, 3, 5, 10, 1] → [1, 3, 4, 10, 5]

#### Code
建構一個heap的樹狀結構（Maxheap），再一個個將值從頭抽出，並重新平衡
- `heapify(arr, n, i)`：函式，將array架構為樹狀結構
    - arr：array
    - n：size of heap，代表node個數，再抽出值後要作調整
    - i ：index，最初的largest，一個個看array內的值
1. 用array想像為tree的結構：利用index來推估孩子的位置
    - index：i (母)
    - left：2 x i + 1 (子)
    - right：2 x i + 2 (子)
2. 先看左邊，若left存在且left值 > largest，則left變成largest
3. 再看右邊，若right存在且right值 > largest，則right變成largest
4. 若largest出現改變，則把old_largest與new_largest的值交換
5. 繼續往下，以new_largest往下看

- `heap_sort(arr)`：用heapifty進行sort
 1. 建立maxheap，讓其達到balance
 2. 一個個抽出
     - 最大值存在index[0]，將其與最後一個值交換，破壞balanece
     - 改變size of heap，讓re-balance不包含前一個balance的最大值
   
    

#### Source
[Heaps and Heap Sort](https://www.youtube.com/watch?v=H5kAcmGOn4Q)

[Heap Sort | GeeksforGeeks](https://www.youtube.com/watch?v=MtQL_ll5KhQ)

[🍟](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#content)

# Try Design heap sort
> H.W.2_Heap Sort
>> Using list：min heap

[👉🏼HERE👈🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_6/Try%20Design%20heap%20sort.py)

- 符合兩個特性：
    1. 完全二元樹（Complete Binary Tree）
       > 披著二元樹羊皮的陣列，用陣列執行較便利
    2. parent > children
       > 僅確保top是整個樹的min或Max，不管兄弟之間是否符合大小排列

- index（從0開始）：
   - left_child：2*i+1
   - right_child：2*i+2
   - parent：(i-1)/2
      > 取整數
      
#### Code


#### Source
[堆排序(Heapsort)](https://www.youtube.com/watch?v=j-DqQcNPGbE)

[heapq --- 堆積佇列 (heap queue) 演算法](https://docs.python.org/zh-tw/3/library/heapq.html)

[[演算法] 堆積排序法(Heap Sort)](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php)

[Heap - 堆](https://algorithm.yuanbin.me/zh-tw/basics_data_structure/heap.html)


[🥯](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#content)

# Test Univalued Binary Tree
> Following blog
>> LeetCode：965. Univalued Binary Tree

[👉🏻HERE👈🏻](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_6/Test%20Univalued%20binary%20tree.py)

Status：Runtime 36 ms, Memory 13.7 MB

針對一個root做判斷，其值是否與左邊值相同，其值是否與右邊值相同，再利用遞迴的方式走訪每個root

#### Source
[【Leetcode_總結】965. 單值二叉樹- python](https://blog.csdn.net/maka_uir/article/details/86021792)

[Leetcode 965：單值二叉樹（最詳細的解法！！！）](https://blog.csdn.net/qq_17550379/article/details/85539683)

[🌭](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#content)

# Try Univalued Binary Tree
> By myself
>> LeetCode：965. Univalued Binary Tree


[🍿](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#content)
