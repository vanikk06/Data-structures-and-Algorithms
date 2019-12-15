
# Graph
  > 圖：由**點＆線**組成

與tree不同，可以有loop（迴路）
  > loop：可以繞回原點（root）
  
- tree是graph的子集合
  - graph：由**點**跟**線**組成，即為graph
  - 在graph中砍掉loop的線，並且點有上跟下的關係，即為tree
    > tree被蘊含在graph中

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_12/image/1576310235203.jpg)

紀錄graph方式：使用array＆linked list
  - array：點
    >　長度：所有的點數
  - linked list：臨邊
    > 以線連接到的其他點
    
    > 不唯一，依據起點的不同，會有不同的linked list
    >> 臨邊必須可以還原graph
    
#### Source
[Graph: Breadth-First Search(BFS，廣度優先搜尋)](http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)

# Breadth-First Search
 > BFS：廣度優先搜尋
 >> 並非最優的走訪方式

 > traversal（走訪）graph
 >> search（搜尋）的必要功能
 
 
#### Step
![](https://upload.wikimedia.org/wikipedia/commons/9/99/Breadth-first_search_Algorithm.gif)

- Step1：從頂點開始，即Level 0
- Step2：查找頂點以單線連接到的所有其他點，這些點即為Level 1
- Step3：假設所有Level 1的點為頂點，查找所有與Level 1以單線相連的其他點，這些點即為Level 2
- Step4：重複上述步驟，直到所有點都被走訪
  
#### Practice
 > by Queue

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_12/image/1576316336720.jpg)
> 無向圖：雙向，無指定特別方向，只要有線連結就要記錄

> graph資料結構：塞入資料就好
>> 無規定由大到小或由小到大：不唯一

使用queue紀錄尚未print出的點
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_12/image/output_aMJs9Q.gif)

#### Source
[圖片來源](https://commons.wikimedia.org/wiki/File:Breadth-first_search_Algorithm.gif)
