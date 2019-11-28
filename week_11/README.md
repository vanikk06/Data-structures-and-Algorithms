# Hash Table
  > 儲存資料的結構
  >> 結合array跟linked list 
 
#### 概念 

在建造Tree時，採用數值大小的比較來決定放置的位置，那如果要放入的資料是字串時，該怎麼辦？
  > Tree因按大小決定儲存位置，從而達到增加**搜尋效率**的效果 
  
 ![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/473px-Hash_table_3_1_1_0_1_0_0_SP.svg.png)
  
Hash Table：所有字串，經過**編碼對應**之後，能將字串的句子轉換為一個**單一**的編碼、編號
  > 不重複的
  
透過follow編碼規則，將字串轉換數值，那就可以對字串進行**排序、比大小**

  
類似dictionary（字典）概念，是以**鍵值-資料對(Key-Value pair)方式**來描述資料的抽象型態
- array：儲存空間，一個抽屜
- linked list：儲存內容物，抽屜裡放的東西
  
- encoding（編碼方式）字串：輸入進電腦時，是我們看得懂得，但當電腦要對其進行運算、處理時，必須將其轉換為數值，而其轉換方式就是依靠**編碼表**的對照

  
- 編碼表：UTF-8、Unicode、BIG-5
   > 約定好的規則
   >> 換碼：對應錯編碼表，查錯位置


