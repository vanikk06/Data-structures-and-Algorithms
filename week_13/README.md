# Content


# Class notes

# Depth-First Search
 > DFS：深度優先搜尋
 
BFS紀錄會與點數（資料個數）成正比，所以空間個數會較高

#### Step
 > 先遇到的就先訪問

- Step1：先遇到的鄰點就先訪問
  > 可使用stack操作
- Step2：以先遇到的鄰點作為新的搜尋起點
  > pop出來的點，要在push其鄰點進去
- Step3：直到所有「有邊相連的鄰點」都被探索過
  > 全部pop出來後，即為結果

#### Practice
 > by stack

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/image/1576310235203.jpg)

DFS：使用**stack**紀錄連結到的其他點
 > code：判斷何時要pop、何時要push 
 
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_13/image/Webp.net-gifmaker1.gif) 


