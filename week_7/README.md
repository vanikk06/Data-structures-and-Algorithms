# H.W.2_Heap Sort & Merge Sort
[🤜🏿HERE🤛🏿](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7/H.W._Heap%20Sort%20%26%20Merge%20Sort)
 - [Heap Sort](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7/H.W._Heap%20Sort%20%26%20Merge%20Sort#heap-sort)
 - [Merge Sort](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7/H.W._Heap%20Sort%20%26%20Merge%20Sort#merge-sort)
 - [Merge Sort vs. Heap Sort](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7/H.W._Heap%20Sort%20%26%20Merge%20Sort#merge-sort-vs-heap-sort)


# Content
- [Including image or picture in jupyter notebook](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7#including-image-or-picture-in-jupyter-notebook)
- [Recursion](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7#recursion)
- [Class notes](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7#class-notes)
- [Merge Sort](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7#merge-sort)
- [Design merge sort](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7#design-merge-sort)
   - [Code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7#code)
   - [Flowchart](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7#flowchart)
   - [Demo](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7#demo)

# Including image or picture in jupyter notebook

- Method 1
  > markdown

  > local圖片；圖檔要在同目錄，若無要標示路徑"/"

```python
![title](image.jpg)  #local圖片
![title](https://example.dot.com/image/picture.jpg)  #網路圖片
```

- Method 2
  > code
 
  > 若不指定長寬，則為原圖大小
 
 ```python
 from IPython.display import Image
 Image(filename="image.jpg", width=400, height=400)
 ```
 
- Method 3
  > markdown：圖片可以居中
      
  ```python
  %%html
  <img src="image.jpg", width=200. height=200>
  ```
  
 - Method 4
   > code：圖片不居中
   
   > %%html：將cell渲染成HTML區塊
   
    ```python
    %%html
    <img src="image.jpg", width=200. height=200>
    ```
    
    >>調整百分比方法：
     ```python
     <img src="image.jpg", width="40%">
     ```
    
#### Source
[Jupyter Notebook：快捷鍵+插入圖片的4種方法](https://www.itread01.com/content/1546717712.html)

[🔨](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7#content)

# Recursion
  > 遞迴
   1. 將一個大問題拆解為重複的眾多小問題
   2. 自我呼叫＆終止條件
   
#### 使用地方：
 - 遇到問題需要回到上一層
 - 解決問題時操作相同但參數不同，需要寫重複程式
   
#### 基本概念
解決問題的方法是[Divide and Conquer](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_4/README.md#divide-and-conquer)

- 性質：函數在執行當中，會不斷**呼叫自己（self-calling）**
  > 要有明確的**終止條件**：避免無止盡自我呼叫
  
  必要條件：
   1. 自我呼叫
   2. 終止條件
   
#### 遞迴限制＆複雜度
缺點
 - 增加時間複雜度：每次input都會遞迴執行，當input增加時，會成**指數**成長
 - 增加空間複雜度：需要很多額外記憶體來儲存待執行步驟與每層執行結果
 
Python對遞迴次數（深度）有所限制，杜絕遞迴無限執行的可能性
> 以此查看python遞迴限制

```python
import sys
sys.getrecursionlimit()   #3000
```
若超過限制，會出現`RecursionError: maximum recursion depth exceeded`


#### Source
[Python 初學第八講 — 遞迴](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-11ed5d300d3d)

[⛏](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7#content)

# Class notes
- 寫程式：訓練「建立問題觀察的拆解能力」
  > 程式：表現的載體
  
- pseudocode：偽碼，看似程式碼但無法編譯執行，僅存在邏輯

[🔧](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7#content)

# Merge Sort
> 從分割中再合併(整合)

> 遞迴

![](https://miro.medium.com/max/450/1*opwN0BhtH4zvPF697fPlow.gif)

| | Design approach | Average Time | Best Time | Worst Time | Extra Space | Stability |
| --- | --- | --- | --- | --- | --- | --- |
|**Merge Sort**| Divide and Conquer | O(n log n) | O(n log n) | O(n log n) | O(n) | Stable |

#### 執行步驟
  > 時間複雜度：O(n log n)
  
- 分割： 將大_list切一半變成兩個小_list，直到不能再分為止（僅剩一個值）
    > 總共切n-1刀，分成n堆

- 合併：將兩個已排序list合併成一個符合排序的大_list
   > 走訪比較、排序
    - 合併兩個已排序list：一一比較每個值，合併n個值就需要n個步驟
    - 合併幾次（幾回合）：每次合併會倆倆合併，每回合減少一半，共要執行log n次
    
 - 時間複雜度：
    - 分割：O(n-1)
    - 合併：O(n log n)
       > n-1 + n log n

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_7/image/1572951110717.jpg)

#### Merge Sort VS. Quick Sort
| | Design approach | Average Time | Best Time | Worst Time | Extra Space | Stability |
| --- | --- | --- | --- | --- | --- | --- |
|**Merge Sort**| Divide and Conquer | O(n log n) | O(n log n) | O(n log n) | O(n) | Stable |
|**Quick Sort**| Divide and Conquer | O(n log n) | O(n log n) | O(n²) | O(n) | UnStable |

- 同：Divide and Conquer，都採用**遞迴**的分割(分堆)再合併，皆需要額外空間
- 異：合併方式不同，所以時間穩定跟穩定度不同
   > Merge Sort 必定是 stable，因為其**不存在交換**
   
#### Source
[Merge sort](https://www.c-programming-simple-steps.com/merge-sort.html)

[Merge Sort 3 – Towards an Implementation (Merge Two Lists)](https://www.youtube.com/watch?v=s8kQm8yhZ8U)

[Merge Sort vs Quick Sort](https://www.youtube.com/watch?v=es2T6KY45cA)

[Merge sort and quick sort](https://www.slideshare.net/MJabin/merge-sort-and-quick-sort)

[圖片來源](https://commons.wikimedia.org/wiki/File:Merge-sort-example-300px.gif)

#### Others
[【硬塞大學生】哈佛校長告訴新生：教育的目標是確保學生能辨別有人在胡說八道](https://www.inside.com.tw/article/10573-harvard-freshman-convocation-address-to-class-2021)

[🔩](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7#content)

# Design merge sort

[👉🏼HERE👈🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_7/Design%20merge%20sort.py)

- 執行步驟
   - 分割：切成兩半，切到不能再切為止(僅剩一個值)
   - 合併：將兩個已排序數列合併
      > 一個元素：只有一個，所以是排序好的

#### Code
分別設計分堆與合併函式，再將兩者放在一起

- `_divide`：分割，不斷將list切成一半，直到剩下一個值為止
   > 考慮長度有基數、偶數兩種情況
      - left：前半部，長度/2的整數
      - right：後半部，剩下的部分
      
     遞迴式，對left、right持續分割，直到剩下一個值，再將它們用_merge函式的方式合併返回
     
- `_merge`：合併且排序
   > 不涉及交換，將兩個已排序list，按小到大順序合併在第三個list
      - temp：用來合併的第三個list
      - n1：left長度
      - n2：right長度
      - i：left的index
      - j：right的index
      
     在left與right的長度內，從第一個值開始一個個比較
      - left < right：將left的值放到temp，繼續比較left的下一個
      - left > right：將right的值放到temp，繼續比較right的下一個
      
     當其中一邊被比完後，不再比較，將剩下的部份一個個放入temp中
      - left被比完：將right剩下的部分一個個放入temp中
      - right被比完：將left剩下的部分一個個放入temp中
      
     回傳最後合併的結果
     
- `merge_sort`：利用_divide與_merge來進行merge sort
      
      
#### Flowchart

- merge_sort

 ![merge_sort](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_7/image/1573233221550.jpg)

- ˍdivide

 ![ˍdivide](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_7/image/1573233373496.jpg)
 
- ˍmerge

 ![ˍmerge](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_7/image/1573233455026.jpg)

#### Demo
 ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_7/image/1573137796982.jpg)

#### Source
[[演算法] 合併排序法(Merge Sort)](http://notepad.yehyeh.net/Content/Algorithm/Sort/Merge/Merge.php)

[初學者學演算法｜排序法進階：合併排序法](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e)

[Merge Sort | GeeksforGeeks](https://www.youtube.com/watch?v=JSceec-wEyw)

[【TBS Learning】演算法-六種排序法之四:合併排序法(merge sort)](https://www.youtube.com/watch?v=KZQbBik3Mew)

[🛠](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_7#content)
