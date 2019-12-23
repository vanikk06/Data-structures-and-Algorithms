# Content 


# Class notes

- 資料結構：如何聰明收納

- 大學：學習「如何學習」的能力
  > 自學
  
  > 獨立性思考
  
- 小技巧：
  - `Tab`：一次往後
  - `shift` + `Tab`：一次往前
  
- 演算法四個條件：
  
  觀察現象，找出能夠作為判斷條件的現象

  1. 合理的開始 
  2. 合理的結束
  3. 找的到下一步
  4. 可找出下一步的方法/動作
   
  
- 在資料庫中，搜尋時會採唯一值（ID）
  

#### Source
[【台灣｜分散式帳本新創BiiLabs】透過IOTA技術應用，可能參與聯合國數位身分專案](https://www.blocktempo.com/taiwan-biilabs-use-iota-building-did-with-un/)

[Blockchain Technology Market Size, Share, & Trends Analysis Report By Type, By Component, By Application, By Enterprise Size, By End Use, By Region, And Segment Forecasts, 2019 - 2025](https://www.grandviewresearch.com/industry-analysis/blockchain-technology-market)

[108課程: 金融科技-文字探勘與機器學習](http://18.217.252.187/%E8%AA%B2%E7%A8%8B%E6%9C%9F%E6%9C%AB%E6%88%90%E6%9E%9C%E7%99%BC%E8%A1%A8/)

[⌚](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_10/README.md#content)

# Red Black Tree
  > 紅黑樹

- [Red Black Tree小遊戲](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_10/README.md#red-black-tree%E5%B0%8F%E9%81%8A%E6%88%B2)
- [觀念](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_10/README.md#%E8%A7%80%E5%BF%B5)
- [Live coding of Rotation](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_10/README.md#live-coding-of-rotation)
- [Red Black Tree vs. Binary Search Tree](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_10/README.md#red-black-tree-vs-binary-search-tree)

BST有可能會弱化成linked list，一旦弱化成linked list，tree的好處（查詢可在O(log n)解決）就消失了

![](https://yotsuba1022.gitbooks.io/data-structure-note/content/assets/rbtree-1.png)

- tree結構：愈balance就可在O(log n)搞定

- BST + rotation = Red Black Tree
  > rotation：旋轉，會回到balance
  >> balance：上一層沒塞滿不能塞下一層

#### Red Black Tree小遊戲
  > 觀察
  
 [✌🏻This🤞🏻](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html)
 
遊戲定義：leaf node的下一個是空集合，將空集合視作黑點，相當於塞滿了null
  > Bug：以root為準，在左子樹發生non-balance的情況下，不會出現rotation

- 在non-balance的情形下，會作rotation
  > non-balance：第n層還沒塞滿就要塞n+1層

- rotation
  > 旋轉
    - right rotation：往右邊轉，讓左邊的點往上抽，右邊的點往下轉
    - left rotation：往左邊轉，讓右邊的點往上抽，左邊的點往下轉
    
    ![](https://upload.wikimedia.org/wikipedia/commons/3/31/Tree_rotation_animation_250x250.gif)

著紅色地方：希望從leaf到root的路徑中黑點個數相同，若不同，則著紅色點
  > rotation條件：將紅點作為rotation的點
  >> 希望維持路徑中黑點個數一樣多，所以紅點僅是**過繼點**


#### 觀念

![](https://yotsuba1022.gitbooks.io/data-structure-note/content/assets/rbtree-2.png)

1. 每個node設為紅色或是黑色
2. root必定為黑色
    > 一定要往下長
3. 若node是紅色，其child必定是黑色
4. 若node是黑色，其child可以是紅色也可以是黑色
5. 每個空node都是黑色
6. 從root到leaf的每條路徑，必定包含相同數目的黑色node
    > rotation觸發機制
    
在node內，還要有一個`.color`的基本屬性，以判斷此為穩定狀態還是有可能被rotation的狀況
  > 紅點、黑點的條件，是觀察出來的現象，可以對rotation下的判斷條件
  - 黑點：穩定狀態
  - 紅點：有可能被rotation
 
利用**黑點數量**來做平衡計算，當non-balance發生黑點數量會不一樣多
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_10/image/1577109453459.jpg)

#### Live coding of Rotation
  > 示範right roration

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_10/image/1577102692121.jpg)

先給一個新的node x（color去繼承原本h的color），去暫存node h的left child（F），原本的h會變成x的right child，最後讓child維持是紅色（rotation後的點就變黑色）
 > 用暫存空間接過node

```python
def rightRotate(self):
  x = self.left
  self.left = x.right #轉
  x.right = self
  
  # color
  x.color = x.right.color
  x.right.color = 'red'
  
  return x
```

#### Red Black Tree vs. Binary Search Tree

兩者皆有「新增」、「刪除」、「查詢」、「修改」，但RBT又增加了「左旋轉」、「右旋轉」跟「著色判斷」
> 有「著色判斷」才可知道，何時要呼叫「左旋轉」，何時要呼叫「右旋轉」
>> 要有兩個小工具：\
    1. 何時改變顏色\
    2. 計算path中有多少黑點
    

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_10/image/1577106909037.jpg)
> 在BST，若root選得不好，就很容易變成linked list（worst case）



#### Source
[Red Black Tree Animation](https://www.youtube.com/watch?time_continue=119&v=rcDF8IqTnyI&feature=emb_logo)

[rotation_圖片來源](https://en.wikipedia.org/wiki/Tree_rotation)

[Red-Black Tree (紅黑樹)](https://yotsuba1022.gitbooks.io/data-structure-note/content/1.4.3-red-black-tree.html)

[維基百科_紅黑樹](https://zh.wikipedia.org/wiki/%E7%BA%A2%E9%BB%91%E6%A0%91)

[Red-Black Tree](http://www.ciaoshen.com/algorithm/2018/11/09/red-black-tree.html)

[Complexity of different tree data structures](https://subscription.packtpub.com/book/application_development/9781786463890/6/ch06lvl1sec63/complexity-of-different-tree-data-structures)

[⏰](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_10/README.md#content)

# Try Find Median from Data Stream
  > LeetCode：295. Find Median from Data Stream

#### Source
[Both O(log(n)) Red-Black Tree solution in Python](https://leetcode.com/problems/find-median-from-data-stream/discuss/74134/both-ologn-red-black-tree-solution-in-python)

[⏱](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_10/README.md#content)
