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
  1. 合理的開始 
  2. 合理的結束
  3. 找的到下一步
  4. 可找出下一步的方法/動作

#### Source
[【台灣｜分散式帳本新創BiiLabs】透過IOTA技術應用，可能參與聯合國數位身分專案](https://www.blocktempo.com/taiwan-biilabs-use-iota-building-did-with-un/)

[Blockchain Technology Market Size, Share, & Trends Analysis Report By Type, By Component, By Application, By Enterprise Size, By End Use, By Region, And Segment Forecasts, 2019 - 2025](https://www.grandviewresearch.com/industry-analysis/blockchain-technology-market)

[108課程: 金融科技-文字探勘與機器學習](http://18.217.252.187/%E8%AA%B2%E7%A8%8B%E6%9C%9F%E6%9C%AB%E6%88%90%E6%9E%9C%E7%99%BC%E8%A1%A8/)

# Red Black Tree
  > 紅黑樹

BST有可能會弱化成linked list，一旦弱化成linked list，tree的好處（查詢可在O(log n)解決）就消失了

- tree結構：愈balance就可在O(log n)搞定

- BST + rotation = Red Black Tree
  > rotation：旋轉，會回到balance
  >> balance：上一層沒塞滿不能塞下一層

#### Red Black Tree小遊戲
  > 觀察
  
 [✌🏻This🤞🏻](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html)

在non-balance的情形下，會作rotation
  > non-balance：第n層還沒塞滿就要塞n+1層

- rotation
  > 旋轉
    - right rotation：往右邊倒，讓左邊變小往右邊轉
    - left rotation：往左邊倒，讓右邊變小往左邊轉
    
   ![](https://upload.wikimedia.org/wikipedia/commons/3/31/Tree_rotation_animation_250x250.gif)

## 紅黑樹
同質無法 轉
 >　資料庫搜尋採唯一值（都當不一樣）
 
 建立小工具，再呼叫
 　著色判斷：何時要左旋轉、右旋轉


#### Source
[Red Black Tree Animation](https://www.youtube.com/watch?time_continue=119&v=rcDF8IqTnyI&feature=emb_logo)

[圖片來源](https://en.wikipedia.org/wiki/Tree_rotation)

[Red-Black Tree (紅黑樹)](https://yotsuba1022.gitbooks.io/data-structure-note/content/1.4.3-red-black-tree.html)

[紅黑樹](https://zh.wikipedia.org/wiki/%E7%BA%A2%E9%BB%91%E6%A0%91)

[Red-Black Tree](http://www.ciaoshen.com/algorithm/2018/11/09/red-black-tree.html)
