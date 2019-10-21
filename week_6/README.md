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


i = o (index)
l = 2*i+1
r = 2*i+2

#### Source
[Heap Data Structure](https://www.geeksforgeeks.org/heap-data-structure/)
