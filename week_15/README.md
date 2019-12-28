# Content

# Adjacency Matrix
  > 鄰接矩陣

# Class notes

- 演算法：生活應用問題的延伸，觀摩演算法的想法可以引起對生活議題的不同看法，重新解構問題，抽象化並一步步歸納解決方法

# Shortest Path
  > 最短路徑：關心**邊**的問題
  >> 此為Dijkstra's Algorithm

常用在路徑規劃中，最小距離的估算方式

計算graph上哪裡有**最短路徑（cost最低）**
  > e.g.Google map的參考路徑：以時間為標的、以費用為標的（是否上高速公路）...
  >> 若將cost轉為價格，尋找價格最低的路徑，時間會拉長\
  >> 若將cost轉為時間，尋找時間最少的路徑，價格會拉高
  
#### § Practice §

起點固定，紀錄走到vertex的cost，若走不到則記錄∞（無限大），再慢慢增加最小cost的vertex，增加的vertex與起點可以共同被取用（可用可不用）
  > 當graph複雜，查看會很困難，使用edge表（包含weight、起點、終點）較優
  
 ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_15/image/output_HGOiV3.gif)

- 若cost大小相同，可自行制定取用順序
  > 相同cost先後沒差，最後結果都會收斂
- 可被取用的vertex，其cost已為最小cost，記錄重複抄寫即可
  > 不須updata
- 新增的vertex重新計算cost的對象，只要考慮新增vertex產生的所有可能path即可，再選出最小的cost
  > 調整過的cost可自行作下標紀錄

#### § Exercise §

#### Source
