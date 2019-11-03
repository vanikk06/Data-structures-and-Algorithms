# Content
 - [Sorting algorithm stability](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#sorting-algorithm-stability)
 - [Heap Sort](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#heap-sort)
    - [Design heap sort](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_6#design-heap-sort)
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

#  Heap Sort
> tree's special case

linked list的變形，每一個node都有且僅有**兩個subnode**，放置順序必為**先左後右**，所有值排完之後，剩下空缺值皆集中在右下方

  > 根據roof值的大小作區分
  
  ![heap sort](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_6/image/1571665085656.jpg)

- Heap Sort：將數列使用Heap結構存入後取出的結果
    > 必定為有排序的
     - 由小到大：Min heap
    - 由大到小：Max heap

- time complexity：穩定的 O(n log n)
   > 有n個值，每個值都要rebalance出一棵樹(O(log n))
   
| | Average Time | Best Time | Worst Time | Extra Space | Stability |
| --- | --- | --- | --- | --- | --- |
|**Heap Sort**| O(n log n) | O(n log n) | O(n log n) | O(1) | Unstable |
> Why heap sort is unstable

- tree資料結構：快速排序、快速搜尋
  > e.g.資料庫：資料存取模式


#### Debug Mode
> Spyder

帶測值進去跑，看它如何運作
- check point：設在細節不理解之處

#### Source
[Heap Data Structure](https://www.geeksforgeeks.org/heap-data-structure/)

[[演算法] 堆積排序法(Heap Sort)](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php)

[Heaps and Heap Sort](https://www.youtube.com/watch?v=H5kAcmGOn4Q)

#### Others
[我以為的軟體工程師九層分級架構](https://ascii-iicsa.blogspot.com/2010/11/blog-post.html)

[推薦書](https://www.books.com.tw/products/0010771263)

# Design heap sort
> Following Teacher's


- index
  - i = n         (母)
  - l = 2 x i + 1 (子)
  - r = 2 x i + 2 (子)

#### Source
[heapq --- 堆積佇列 (heap queue) 演算法](https://docs.python.org/zh-tw/3/library/heapq.html)

[Heap Sort: how to sort?](https://stackoverflow.com/questions/13979714/heap-sort-how-to-sort)

[Heap Sort | GeeksforGeeks](https://www.youtube.com/watch?v=MtQL_ll5KhQ)

[Heap - 堆](https://algorithm.yuanbin.me/zh-tw/basics_data_structure/heap.html)


# Test Univalued Binary Tree
> Following blog
>> LeetCode：965. Univalued Binary Tree

[👉🏻HERE👈🏻](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_6/Test%20Univalued%20binary%20tree.py)

針對一個root做判斷，其值是否與左邊值相同，其值是否與右邊值相同，再利用遞迴的方式走訪每個root

#### Source
[【Leetcode_總結】965. 單值二叉樹- python](https://blog.csdn.net/maka_uir/article/details/86021792)

[Leetcode 965：單值二叉樹（最詳細的解法！！！）](https://blog.csdn.net/qq_17550379/article/details/85539683)


# Try Univalued Binary Tree
> By myself
>> LeetCode：965. Univalued Binary Tree

