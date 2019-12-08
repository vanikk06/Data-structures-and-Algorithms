# Content
- []()
- [Hash TableⅠ](#hash-table%E2%85%B0)
- [Hash TableⅡ](#hash-table%E2%85%B1)
- [Test Desigh HashSet](#test-desigh-hashset)
    - [Code](#code)
- [Try Desigh HashSet](#try-desigh-hashset)
    - [Changing of capacity](#changing-of-capacity)
    - [Changing of code](#changing-of-code)


# Encoding
 > 編碼、加密
 
 
 
#### Source
[Python資料加密，解密的相關操作（hashlib、hmac、random、base64、pycrypto）](https://www.itread01.com/content/1542966064.html)


# Hash TableⅠ
  > class teaching

  > 儲存資料的結構
  >> 結合array跟linked list 
  
- [概念](#-%E6%A6%82%E5%BF%B5-)
- [資料結構](#-資料結構-)
- [hash function](#-hash-function-)
- [MD5 hash](#-md5-hash-)
- [字串格式轉換](#-%E5%AD%97%E4%B8%B2%E6%A0%BC%E5%BC%8F%E8%BD%89%E6%8F%9B-)
 
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

#### Others
[Pair Programming](https://www.youtube.com/watch?v=vgkahOzFH2Q&feature=youtu.be)

[🏳‍🌈](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/README.md#content)

# Hash TableⅡ
  > online information
  
- [mapping](#mapping)
- [Hash Table](#hash-table)
    - [時間複雜度](#%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6)
    - [不適用Hash Table](#不適用hash-table)

  
#### mapping
  > 映射：使用鍵值（key）去查詢資料內容（value）

e.g. array：利用index對應到儲存的資料
  - key只能是**非負整數**
    > 必須在index範圍內（0 ~ n-1）
  - 儲存資料的型別**不受限制**
    > Python：對應到的是儲存空間，而非資料本身（一個array可以儲存一個以上的資料型別）
    
#### Hash Table
  > 雜湊表：將key轉成index搜尋
  > 解決mapping問題

Hash Table是透過hash function將給定的key對應到一個index後，將value存放到對應的位置（bucket）
 > key不限制只能是非負整數
 
 > **兩次**對應：
 >> 1. key對應到index
 >> 2. index對應到value
 
- hash function：將每個key**對應**到一個固定的index
    > 將字串編碼
    
    > 位元運算：不在意資料型別

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/image/1575746923024.jpg)

理想中的hash table是所有的index都只對應到單一個key，但實際上並非如此
- collision：碰撞，兩個以上的key對應到相同的index
    > 可使用linked list或是BST
        
#### 時間複雜度：
|   | Best | Worst |
| --- | --- | --- |
| **Time complexity** | O(1) | O(n) |

- Best：O(1)，將key運算得到index，直接到index找資料
 > 一個index只對應到一個key
 >> 當資料量大時，若想達到這點，需要犧牲大量的記憶體空間（增加index個數）
 
- Worst：O(n)，所有key都對應到相同的index
  
#### 不適用Hash Table
- 有時間順序的
    > queue better

- 對data進行排序
    > hashSet是**字典**對應的資料結構
    
#### Hash function

#### Source
[【C++ 資料結構與演算法】雜湊表 (hash table)](https://www.youtube.com/watch?v=O4dGJZ4J0Bk&t=)

[白話的 Hash Table 簡介](https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/)

[hash function 觀念和實務](https://hackmd.io/@EW34LLeXTra2Oikg0WEQ5Q/HJln3jU_e?type=view)

[Hash Table：Intro(簡介)](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html)

[What Is Bitcoin Hashing? Hash Functions Explained Simply !!](https://themoneymongers.com/bitcoin-hash/)

[What is Hashing? Hash Functions Explained Simply](https://www.youtube.com/watch?v=2BldESGZKB8&feature=emb_logo)

[🏴‍☠️](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/README.md#content)

# Test Desigh HashSet
  > Following teacher's
  >> LeetCode：705. Design HashSet

[👉🏼HERE👈🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/Test%20Design%20HashSet.py)

Status：Runtime 2824 ms, Memory 17.9 MB

利用array跟linked list來達到hash table的資料結構
  - 增加node是加在linked list第一個
  - 移動指標，判斷式為node是否存在（node存在就往下一個移動）
     > 不會出現`AttributeError`

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
      
        - No：進入while迴圈
          >　查看input是否與已存的值相同
          - 是否相同
            > 相同值只存取一次
             - Yes：返回
             - No：node指標指到下一個node
        - Yes：跳出while迴圈，建立一個新的node，放到linked list的第一個
      
  - `remove`：移除HashSet內的資料，若資料不存在則不作為
  
     先將input除以array長度，找到其存放的index，再將index的值存到另一個變數（node）方便操作
      - 如果node存在 且 node的值等於目標刪除值：將node指標的下一個node重新存入index中，返回
      
      建立另一個變數（pre），存入node的前一個node，方便刪除（重新建立連結）
      
      - node是否為None
        - No：進入while迴圈
          > 尋找目標刪除值
          - node的值是否與目標刪除值相同
            - Yes：重新建立連結，返回
            - No：node指標與pre指標皆指到下一個
        - Yes：跳出while迴圈，不處理
      
  - `contains`：資料是否存在HashSet內，回傳True或False
    
     先將input除以array長度，找到其存放的index，再將index的值存到另一個變數（node）方便操作
     - node是否為None
        - No：進入while迴圈
          > 尋找目標搜尋值
          - node的值是否與目標搜尋值相同
            - Yes：返回True
            - No：node指標指到下一個node
        - Yes：返回False

[🏁](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/README.md#content)
        
# Try Desigh HashSet
  > By myself：更改H.W.4_Hash Table
  >> LeetCode：705. Design HashSet

根據此題LeetCode對作業四的程式碼進行更改

- [Changing of capacity](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/README.md#changing-of-capacity)
- [Changing of code](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/README.md#changing-of-code)
  
## Changing of capacity
[👉🏼HERE👈🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/Try%20Design%20HashSet_Changing%20of%20capacity.py) 

🚫 Status：Time Limit Exceeded
  > 計算太久
  >> 有可能是Bug引起的，若不是則是演算法計算太慢，要重新思考計算方式

此處code會出現`Time Limit Exceeded`的問題，除了演算法設計太過繁瑣外，還有一個原因是因為capacity設定的太小（原始設定為5），才會導致即使使用Hash Table的資料結構仍出現計算過久的問題

- 將capacity更改為7：測資皆通過但是仍花過長時間

  🚫 Status：Time Limit Exceeded
    > 28 / 28 test cases passed, but took too long.

- 將capacity更改為8：Accepted

  Status：Runtime 2596 ms, Memory 17.8 MB
  
#### Source
[LeetCode介紹](https://arton0306blog.wordpress.com/2018/04/15/leetcode%E4%BB%8B%E7%B4%B9/)

[🏳](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/README.md#content)

## Changing of code
[👉🏼HERE👈🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/Try%20Design%20HashSet_Changing%20of%20code.py)

[🏴](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/README.md#content)
