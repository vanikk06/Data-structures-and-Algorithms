# Hash Table
  > 儲存資料的結構
  >> 結合array跟linked list 
 
#### § 概念 § 

在建造Tree時，採用數值大小的比較來決定放置的位置，那如果要放入的資料是字串時，該怎麼辦？
  > Tree因按大小決定儲存位置，從而達到增加**搜尋效率**的效果 
  
 ![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/473px-Hash_table_3_1_1_0_1_0_0_SP.svg.png)
  
Hash Function：所有字串，經過**編碼對應**之後，能將字串的句子轉換為一個**單一**的編碼、編號
   
   - 特性：
      - Unique hash value：不同的input不可能產生相同的hash value，相同的input只會產生相同的hash value
      - High hashing speed：速度快
      - Secure hash function：安全，修改困難（修改=input不同，會產生不同的hash value）  
  
透過follow編碼規則，將字串轉換數值，那就可以對字串進行**排序、比大小**，這次使用有別於Tree的資料結構儲存

#### § 資料結構 §
   > 將資料**打散**，每堆資料之間的落差不會太懸殊   
   >> 目的：增加搜尋效率
   
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/image/1574970681652.jpg)   
  
類似dictionary（字典）概念，以**鍵值-資料對(Key-Value pair)方式**來描述資料的抽象型態
- array：儲存空間，一個抽屜
- linked list：儲存內容物，抽屜裡放的東西

重新編碼後的字串會產生一個數字，將其塞入對應的array中
  > e.g. 有100筆資料，1到100，將其放入長度16的array中（index:0 ~ 15），使用除法**餘數**的方式：\
  餘數為0 → index 0\
  餘數為1 → index 1\
  餘數為2 → index 2...以此類推下去\
  將資料放入array中，若遇到資料重複堆疊的情形，就用linked list的方式放在第一個資料的next\
  （在array index 1中儲存的是一條linked list，head是1，next是17...）
  >> 所以，在長度16的array會有16條linked list，index 1到index 4會有7個node，其餘皆有6個node

  - 優點：搜尋有效率，可以先判斷是哪堆，再進去搜尋


#### § hash function §
  > **字串跟數值**的轉換

- encoding（編碼方式）字串：輸入進電腦時，是我們看得懂得，但當電腦要對其進行運算、處理時，必須將其轉換為二進位數值，電腦才有辦法進行處理，而其轉換方式就是依靠**編碼表**的對照
  > 通電：1，沒通電：0，通過通電&沒通電來告訴電腦，現在要做什麼行為

    - 編碼表：UTF-8、BIG-5
       > 約定好的規則
       >> 亂碼：對應錯編碼表，查錯位置

    - 字元 vs. 字串
      - 字元：有限，編碼表編譯對象
          > e.g.英文字母
      - 字串：無限增生
  
- hash：將每個字元對應到編碼表後，再去作數學運算
  > 概念，將**字串**對應到**數值**的方法
  >> 讓明文跟密文不會被輕易破解

  - [MD5](https://www.ez2o.com/App/Coder/MD5)：將字元轉為字串（string），再將字串編到一個新的編碼，且確保此編碼唯一
    > Two-way function，可逆的
        
 ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/image/1575142526928.jpg)

#### § MD5 hash §
  > hash編碼的一種方式
  
  > 更改小部分，編碼變動會很大
  >> 保護資料：更改會被知道

透過特定規則的邏輯運算可以將字串轉變為數值，且其為唯一，不會有重複的機會

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/image/1574970350704.jpg)

在input近來前，會先有一組初始值（外部給定），進入邏輯運算
> 將字元(input)轉為十六進位編碼，再轉成二進位去作邏輯運算，之後湊出的編碼
- 邏輯運算：F、G、H、I
  > B、C、D = X、Y、Z


#### § 字串格式轉換 §
|   | 2進位制 | 8進位制 | 10進位制 | 16進位制 |
| --- | --- | --- | --- | --- |
| **2進位制** | - | bin(int(x, 8)) | bin(int(x, 10) | bin(int(x, 16)) |
| **8進位制** | oct(int(x, 2)) | - | oct(int(x, 10)) | oct(int(x, 16) |
| **10進位制** | int(x, 2) | int(x, 8) | - | int(x, 16) |
| **16進位制** | hex(int(x, 2)) | hex(int(x, 8)) | hex(int(x, 10)) | - |


#### Source
[Wikipedia - Hash table](https://en.wikipedia.org/wiki/Hash_table)

[What Is Bitcoin Hashing? Hash Functions Explained Simply !!](https://themoneymongers.com/bitcoin-hash/)

[What is Hashing? Hash Functions Explained Simply](https://www.youtube.com/watch?v=2BldESGZKB8&feature=emb_logo)

[Hash Table | A Helpful Line-by-Line Code Tutorial](https://www.youtube.com/watch?v=aZVNWYSR_sY&feature=emb_logo)

[MD5 Hash](http://practicalcryptography.com/hashes/md5-hash/)

[MD5.py](https://github.com/timvandermeij/md5.py/blob/master/md5.py)

[9. Hash Sets](https://www.cs.wcupa.edu/rkline/ds/hash-sets.html)

[白話的 Hash Table 簡介](https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/)


# Test Desigh HashSet
  > Following teacher's → LeetCode：705. Design HashSet

[👉🏼HERE👈🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/Test%20Design%20HashSet.py)

Status：Runtime 2824 ms, Memory 17.9 MB

利用array跟linked list來達到hash table的資料結構

#### Code

- Mynode：linked list基本屬性
  - .val：node內的資料
  - .next：node與下一個node的連結

- MyHashSet：結合array與linked list
  - `__init__`：array基本屬性
    - .capacity：array長度，有幾個index
    - .data：建立capacity長度的array，以儲存資料
  -  `add`：在HashSet內插入資料
    先將input除以array長度，找到其存放的index，再將index的值存到另一個變數（node）方便操作
    - node是否為None
      > None必為False
      >> - 若index本身是空的，其值是None
      >> - 若node不存在，其也為None
