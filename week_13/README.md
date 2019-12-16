# Content

# if__name__ == __main__
 > 當主程式時再跑，import時不跑
 
 > 21:20

利用if將class以外的主程式包起來，若此檔案並非成主程式，即不執行

#### Source
[Python - if __name__ == '__main__' 涵義](http://blog.castman.net/%E6%95%99%E5%AD%B8/2018/01/27/python-name-main.html)

[Python之父教你寫main()函數](https://codingpy.com/article/guido-shows-how-to-write-main-function/)

# Class notes
- 達克效應（Dunning-Kruger effect）

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/image/1576490058855.jpg)

- John Dewey

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/image/1576490775235.jpg)


# Depth-First Search
 > DFS：深度優先搜尋
 
BFS紀錄會與點數（資料個數）成正比，所以空間個數會較高

#### Step
 > 先遇到的就先訪問

- Step1：先遇到的鄰點就先訪問
  > 可使用stack操作
- Step2：以先遇到的鄰點作為新的搜尋起點
  > pop出來的點，要在push其鄰點（list）進去
- Step3：直到所有「有邊相連的鄰點」都被探索過
  > 全部pop出來後，即為結果

#### Practice
 > by stack

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/image/1576310235203.jpg)

DFS：使用**stack**紀錄連結到的其他點
 > code：判斷何時要pop、何時要push 
 
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/image/Webp.net-gifmaker1.gif) 

- 如何判斷值已經處理過：
 將push進stack的值做註記，通常使用染色
  > 若要進入stack判斷：可在stack進行contain
  >> 原始stack不存在此功能


# BFS vs. DFS
 > 35:00

|  | Design | Time Complexity |
| --- | --- | --- |
| **BFS** | Queue | O(V+E) |
| **DFS** | Stack| O(V+E) |
> 時間複雜度：有多少**鄰邊＆點**
>> 必須全部走完

兩者時間接花在處理queue/stack上，但queue/stack的時間複雜度是相同的

差異：需要的記憶體空間
 > 時間＆記憶體空間是相對的
 
 - BFS：把點逐個加入queue，通常需要與**點數**成正比的記憶體空間
 - DFS：與**遞迴深度**成正比，與點數相比，遞迴深度並不大
   > 在pop過程，不會保留過多的記憶體空間
 
 
