
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
  - linked list：臨邊
    > 以線連接到的其他點



# 黑板
> 圖 資料結構：塞入資料就好
>> 無規定由大到小或由小到大：不唯一

先將關係畫成圖，再確定走訪順序
