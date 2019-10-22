# Sorting Algorithm Stability

#### Source
[判斷各種排序演算法的穩定性](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/548443/)


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

- index
  - i = n         (母)
  - l = 2 x i + 1 (子)
  - r = 2 x i + 2 (子)

#### Source
[heapq --- 堆積佇列 (heap queue) 演算法](https://docs.python.org/zh-tw/3/library/heapq.html)

[Heap Sort: how to sort?](https://stackoverflow.com/questions/13979714/heap-sort-how-to-sort)

[Heap Sort | GeeksforGeeks](https://www.youtube.com/watch?v=MtQL_ll5KhQ)


# Test Univalued Binary Tree
> LeetCode：965. Univalued Binary Tree

> Queue資料結構

#### Source
[【LeetCode】965. Univalued Binary Tree 解題報告（Python & C++）](https://blog.csdn.net/fuxuemingzhu/article/details/85385974)
