# Recursion
  > 遞迴
  

#### Source
[Python 初學第八講 — 遞迴](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-11ed5d300d3d)

# Class notes
- 寫程式：訓練「建立問題觀察的拆解能力」
  > 程式：表現的載體
  
- pseudocode：偽碼，看似程式碼但無法編譯執行，僅存在邏輯

# Merge Sort
> 從分割中再合併(整合)
- 分堆： 分兩堆兩堆，要分log n次才會分完
  > 時間複雜度：O(n log n)
  >> 每個分出的堆都要重新比較，共分出n堆
- 合併：將分堆結果比較合併
   > 走訪比較、合併

| | Design approach | Average Time | Best Time | Worst Time | Extra Space | Stability |
| --- | --- | --- | --- | --- | --- | --- |
|**Merge Sort**| Divide and Conquer | O(n log n) | O(n log n) | O(n log n) | O(n) | Stable |

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_7/image/1572951110717.jpg)

#### Merge Sort VS. Quick Sort
- 同：遞迴的分割再合併，皆需要額外空間
- 異：合併方式不同

#### Source
[Merge sort](https://www.c-programming-simple-steps.com/merge-sort.html)

[Merge Sort 3 – Towards an Implementation (Merge Two Lists)](https://www.youtube.com/watch?v=s8kQm8yhZ8U)

[Merge Sort vs Quick Sort](https://www.youtube.com/watch?v=es2T6KY45cA)

[Merge sort and quick sort](https://www.slideshare.net/MJabin/merge-sort-and-quick-sort)

#### Others
[【硬塞大學生】哈佛校長告訴新生：教育的目標是確保學生能辨別有人在胡說八道](https://www.inside.com.tw/article/10573-harvard-freshman-convocation-address-to-class-2021)

# Design Merge sort

#### Source
[[演算法] 合併排序法(Merge Sort)](http://notepad.yehyeh.net/Content/Algorithm/Sort/Merge/Merge.php)

[初學者學演算法｜排序法進階：合併排序法](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e)

[Merge Sort | GeeksforGeeks](https://www.youtube.com/watch?v=JSceec-wEyw)

[【TBS Learning】演算法-六種排序法之四:合併排序法(merge sort)](https://www.youtube.com/watch?v=KZQbBik3Mew)
