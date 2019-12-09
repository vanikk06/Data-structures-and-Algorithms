# Content
- [Coding](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/README.md#coding)
- [Hash Table Ⅰ](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_11#hash-table-%E2%85%B0)
- [Hash Table Ⅱ](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_11#hash-table-%E2%85%B1)
- [BlockChain](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_11#blockchain)
- [BitCoin Hashing](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_11#bitcoin-hashing)
- [Test Desigh HashSet](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_11#test-desigh-hashset)
    - [Code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_11#code)
- [Try Desigh HashSet](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_11#try-desigh-hashset)
    - [Changing of capacity](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_11#changing-of-capacity)
    - [Changing of code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_11#changing-of-code)


# Coding
 > 資料加密
 
網路資料的風險
 - 資料竊聽與機密性：該如何保證資料不會因被攔劫或竊聽而暴露
 - 資料篡改與完整性：該如何保證資料不會被惡意篡改
 - 身份冒充與身份驗證：該如何保證資料互動的雙方身份沒有被冒充
 
針對以上問題，有幾種資料加密的方式來解決（每種資料加密方式又有多種不同的演算法實現）：

| 資料加密方式 | 描述 | 主要解決問題 | 常用演算法 |
| --- | --- | --- | --- |
| **對稱加密** | 資料加密＆解密使用相同的金鑰 | 資料的機密性 | DES、AES |
| **非對稱加密** | 資料加密＆解密使用不同的金鑰（金鑰對） | 身份驗證 | DSA、RSA |
| **單向加密** | 只能加密資料，而不能解密資料 | 資料的完整性 | MD5、SHA系列 |
 > 非對稱加密又稱**公鑰加密**
 
 > SHA系列演算法，是根據生成的編碼（密文）的長度而命名名稱
 >> e.g. SHA1（160 bits）、SHA256
 
#### Source
[Python資料加密，解密的相關操作（hashlib、hmac、random、base64、pycrypto）](https://www.itread01.com/content/1542966064.html)

[🚦](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/README.md#content)

# Hash Table Ⅰ
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
  >> 編碼長度為128 bits
  
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

[MD5 Hash](http://practicalcryptography.com/hashes/md5-hash/)

[MD5.py](https://github.com/timvandermeij/md5.py/blob/master/md5.py)

[9. Hash Sets](https://www.cs.wcupa.edu/rkline/ds/hash-sets.html)

#### Others
[Pair Programming](https://www.youtube.com/watch?v=vgkahOzFH2Q&feature=youtu.be)

[🏳‍🌈](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/README.md#content)

# Hash Table Ⅱ
  > online information
  
  > 資料結構：使用**字典**的方式儲存資料，優於查詢
  >> {key：value} pair：鍵值-資料對
  
- [mapping](#mapping)
- [Hash Table](#hash-table)
    - [時間複雜度](#%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6)
    - [不適用Hash Table](#不適用hash-table)
- [Hash function](#hash-function)
    - [Hash function of property](#hash-function-of-property)
    - [Division Method](#division-method)
    - [Multiplication Method](#multiplication-method)

  
#### mapping
  > 映射：使用鍵值（key）去查詢資料內容（value）

e.g. array：利用index對應到儲存的資料
  - key只能是**非負整數**
    > 必須在index範圍內（0 ~ n-1）
  - 儲存資料的型別**不受限制**
    > Python：對應到的是儲存空間，而非資料本身（一個array可以儲存一個以上的資料型別）
    
#### Hash Table
  > 雜湊表：將key轉成index搜尋
  > 解決mapping問題，避免浪費記憶體空間

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
    > 可能使用到的key之數量大於table大小
        
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
  > 將任何長度的input利用數學函式**轉換**（convert）為固定大小的字符串的一個過程
  >> 讓key對應到符合table大小的index
  >> 字符串：numbers and letters

input + Hash function = Hash value

- input：任意長度
- Hash function：轉換過程，密碼學
   > 此種轉換為一種**壓縮對應**，hash value通常遠小於input的空間
- Hash value：固定長度、大小



理想的hash function，應該具備兩個特點：
 > time complexity：O(1)
   - 定義域（domain）為整個key的集合，值域（range）應小於table的大小
       > domain：所有可能的input
       
       > range：key對應到的index是在table內
   - 盡可能讓key經過hash function後，在range（index）能夠平均分佈（uniform distributed），如此才不會有collision的情形

#### Hash function of property

1. Unique：不同的input不可能產生相同的hash value，相同的input只會產生相同的hash value
2. High hashing speed：對任何的input，轉換速度皆是快的
3. Secure hash function：安全，逆轉該函式或是將其設為雙向是困難的
    > input中的微小變化，會產生完全不同的hash value
    >　雙向：input和output之間可以自由轉換

#### Division Method
   > 除法：table大小有限制，但速度較快
   
將大範圍的key對應到小範圍的table，最直覺的作法就是利用**modulus(mod)取餘數**
 > modulus模除：除法取餘數

e.g. table大小為8，則key與table之index對應關係如下：\
  14 mod 8 = 6 → index 6\
  23 mod 8 = 7 → index 7\
  16 mod 8 = 0 → index 0\
  50 mod 8 = 2 → index 2
  
- 優點：快速，只要做一次餘數（除法運算）即可
- 缺點：table大小限制，容易發生collision
    > 理想的table大小是「距離2<sup>p</sup>夠遠」的質數，像是701
    >> table大小必須慎選，要盡量避開2的指數（2<sup>p</sup>），否則就只有「最低位的p-bit」會影響hash function的結果，以table大小為8 = 2<sup>3</sup>為例，key mod 2<sup>3</sup>的意思是，只取「以二進位表示的key的最低位的**3個bit**」來決定key對應到的table之index\
    ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/image/1575883266177.jpg)\
    在這種情況下，若有大量變數以相同的命名規則（e.g. a_count、b_count、c_count...），很可能在將字串轉換成key時，得到「低位bit」完全相同的key，因而將三個變數都對應到相同的index導致collision

#### Multiplication Method
   > 乘法：table大小無限制，但速度較慢
   
在實際面對資料時，時常無法預先得知「key的範圍」與「在該範圍內key的分佈情形」，在此前提下，不需要避開特定的table大小的multiplication method會比較優

方法如下：
![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/image/1575885467652.jpg)

key：K，size of table：m = 2<sup>p</sup>
1. 選擇常數A
    > A介於0到1之間（0 < A < 1）
2. 將K乘以A，得到KA
3. 取KA的小數點部分f
    > f = KA - ⌊KA⌋ 
    >> ⌊ ⌋：向下取整數 
4. 將f乘上m，得到mf
5. 取整數部分，h(Key) = ⌊mf⌋ = ⌊m(KA-⌊KA⌋)⌋  

- 優點：能夠盡量把更多的key之bit納入考慮，得到對應的table之index
   > 隨機性增加

#### Source
[【C++ 資料結構與演算法】雜湊表 (hash table)](https://www.youtube.com/watch?v=O4dGJZ4J0Bk&t=)

[白話的 Hash Table 簡介](https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/)

[hash function 觀念和實務](https://hackmd.io/@EW34LLeXTra2Oikg0WEQ5Q/HJln3jU_e?type=view)

[Hash Table：Intro(簡介)](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html)

[What is Hashing? Hash Functions Explained Simply](https://www.youtube.com/watch?v=2BldESGZKB8&feature=emb_logo)

[Hash Table | A Helpful Line-by-Line Code Tutorial](https://www.youtube.com/watch?v=aZVNWYSR_sY&feature=emb_logo)

[Python資料加密，解密的相關操作（hashlib、hmac、random、base64、pycrypto）](https://www.itread01.com/content/1542966064.html)

[🏴‍☠️](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/README.md#content)

# BlockChain
  > 區塊鏈
  
  > 技術，互聯網上記錄數據的全新方式 

在區塊鏈中，hash被用來表示blockchain的**當前狀態**，並確保他是**不會被更改的**

每筆交易都含有特定的信息，例如數量、送貨地址、到貨地址...，所有這些訊息都會被組合在公式中，產生稱為"Transaction ID"的hash value，可用來識別和確認交易已經發生

在blockchain中的第一塊被稱為Genesis Block，包含交易的訊息，當他們被組合在一起時會產生唯一的hash value，當第二塊創建時，Genesis Block的hash value會被加到新block中的所有新交易，再以新組合產生各自的hash value，重複此行動作在所有blockchain中的block

如此，採用舊的hash value產生新的hash value，從而建造block之間牢不可破的**依賴關係**，每個block都鏈接到其先前的block，以此讓blockchain成為**安全、透明、不變的網絡**


#### Source
[What is Hashing? Hash Functions Explained Simply](https://www.youtube.com/watch?v=2BldESGZKB8&feature=emb_logo)

[What is Blockchain?](https://lisk.io/what-is-blockchain)

[🚩](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/README.md#content)

# BitCoin Hashing
  > 比特幣
  
經過hash function產生的output稱為hash，是一種**加密產品**

hash function可以分為兩種類型：
 - One-way function：對於給定的input，很容易產生output，但即使知道output也無法找到input
    > 回溯input是不可能的
    
    > input改變output必然改變
 - Two-way function：當input跟output已知時，往返兩者是容易的
 
 
在bitcoin中使用的hash function是更為重要且更為複雜的，它使用One-way function （e.g.SHA-256）

#### SHA-256
   > bitcoin's blockchain主要的hash function

特性：
1. Unique hash value
2. High hashing speed
3. Secure hash function

bitcoin是利用hashes作的數字分類帳，它利用工作量證明（proof of work）與SHA-256結合來獲得數學上的可追溯性（mathematical traceability）和不可破解性（unbreakability）

- Bitcoin Mining：確保上述過程
  > 挖礦

#### Source
[What Is Bitcoin Hashing? Hash Functions Explained Simply !!](https://themoneymongers.com/bitcoin-hash/)

[Blockchain Basics Explained - Hashes with Mining and Merkle trees](https://www.youtube.com/watch?v=lik9aaFIsl4&feature=youtu.be)

[🚧](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/README.md#content)

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

Status：Runtime 2592 ms, Memory 17.8 MB
 > 在capacity為6的情況下可以通過，但5時仍會超時
 
⭐在移動node指標時，最簡化的判斷是直接判斷**node本身**是否存在
 > 若以node.val或node.next進行判斷，容易將node指標走到不存在的node，為此就需要很多額外的判斷式來補足這點

#### Code
 更改`add`與`remove`部分
 
 - `add`：以**node本身是否存在**作為node指標移動的判斷，並增加一個變數pre，以在linked list的最後面增加新資料
    
    先將input除以capacity找到存放的index，再將存放在index的資料放到node指標方便走訪，並設置一個變數pre存放node指標的前一個node
    - 判斷node是否存在
        - Yes：進入while迴圈
            - input是否已存在於linked list內：
                - Yes：返回
                - No：node指標與pre指標往下一個移動
        
         跳出while迴圈，pre指標指在linked list的最後一個node
        - pre指標是否為None：
            - Yes：在index內創造一個值是input的node
              > index本身為None，沒有進入while迴圈，所以直接加
            - No：在pre指標的下一個node創造一個值為input的新node
                     
 - `remove`：以**node本身是否存在**作為node指標移動的判斷
 
    先將input除以capacity找到存放的index，再將存放在index的資料放到node指標方便走訪，並設置一個變數pre_node存放node指標的前一個node，方便移除重新建立連結
    
    - 先判斷目標移除值是否是第一個node：
        - Yes：將node指標的下一個node重新存入index中
    - 判斷node是否存在：
        - Yes：進入while迴圈
            - node指標是否為目標移除值
                - Yes：重新建立連結，pre_node指標的下一個連接到node指標的下一個
                - No：node指標與pre_node指標皆往下一個node移動
         
         跳出while迴圈，代表目標移除值不存在，返回

[🏴](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11/README.md#content)
