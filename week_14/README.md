# Content
 - [split](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#split)
 - [Iterators](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#iterators)
 - [Python: range is not an iterator!](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#python-range-is-not-an-iterator)
 - [Generator](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#generator)
 - [＿＿name＿＿](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#%EF%BC%BF%EF%BC%BFname%EF%BC%BF%EF%BC%BF)
 - [python –](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#python-)
 - [List Comprehension](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#list-comprehension)
 - [sort vs. sorted](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#sort-vs-sorted)
 - [key vs. value](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#key-vs-value)
 - [Greedy Algorithm](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#greedy-algorithm)
 - [Disjoint Sets](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#disjoint-sets)
 - [Minimum Spanning Tree](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#minimum-spanning-tree)
 - [Adjustment of Design Kruskal](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#adjustment-of-design-kruskal)

# split
  > 拆分字串
  
在python中拆解字串有兩個函式：
- `split()`：通過**指定分割符**對字串進行切片，並回傳分割後的字串list
   > str.split(str=” “, num=string.count(str))[n]
   
   - str：分隔符，預設為空格，若字串中沒有分隔符，則將整個字串作為list的一個元素
     > ""內不能是空的，會出現`ValueError`
   - num：分割次數，若存在num參數，則會分割為 num+1 個子字串，並且每個子字串可以賦予給新的變數
     > 為-1時，與預設相同
   - [n]：選取第n個子字串
     > 注意！當使用空格作為分割符時，空的項會被自動忽略

   [✍🏻](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#split-1) 

- `os.path.split()`：**按照路徑**將文件名和路徑分割開
   > os.path.split('PATH')
   
   - PATH：一個文件的全路徑
       - 如果參數是「一個目錄和文件名」：回傳 路徑＆文件名
       - 如果參數是「一個目錄名」：回傳 路徑＆為空的文件名
   
   [✍🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#ospathsplit)
   
另外還有一個函式`rsplit()`，類似於`split()`只是是從字串最後面開始分割

- `rsplit()`：從**最後面**開始，通過**指定分隔符**對字串進行切割
   > str.rsplit(sep=None, count=S.count(sep))
   
   - sep：分割符，預設為空格
     > 包含空格、換行(\n)、Tab(\t)
   - count：分割次數，預設為分割符在字串中出現的總次數
   
   [✍🏽](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#rsplit)

#### 實例

###### split()

常用實例
```python
u = "www.doiido.com.cn"

print(u.split())      #分割符：空格(預設)
                      #字串內不存在分割符，回傳一個元素(字串本身)

print(u.split('.'))   #分割符：.
                      #不限制分割次數
                      
print(u.split('.',0)) #分割符：.
                      #分割次數：0，回傳0+1個元素
          
print(u.split('.',1)) #分割符：.
                      #分割次數：1，回傳1+1個元素

print(u.split('.',2)) #分割符：.
                      #分割次數：2，回傳2+1個元素
                      
print(u.split('.',2)[2]) #分割符：.
                         #分割次數：2，回傳2+1個元素
                         #並取index為2的項
 
print(u.split('.',-1)) #分割符：.
                       #分割次數：最多次，與未限制相同
```
輸出：
```python
['www.doiido.com.cn']
['www', 'doiido', 'com', 'cn']
['www.doiido.com.cn']
['www', 'doiido.com.cn']
['www', 'doiido', 'com.cn']
com.cn
['www', 'doiido', 'com', 'cn']
```

去調換行符
```python
c = '''say
hello
baby'''

print(c)

print(c.split('\n'))
```
輸出：
```python
say
hello
baby

['say', 'hello', 'baby']
```

###### os.path.split()

分離文件名和路徑
```python
import os

print(os.path.split('/dodo/soft/python/'))  #目錄
print(os.path.split('/dodo/soft/python'))   #目錄+文件名
```
輸出：
```python
('/dodo/soft/python', '')
('/dodo/soft', 'python')
```

超級好的例子
```python
s="hello boy<[www.doiido.com]>byebye"

print(s.split("[")[1].split("]")[0])
print(s.split("[")[1].split("]")[0].split("."))
```
輸出：
```python
www.doiido.com
['www', 'doiido', 'com']
```

###### rsplit()

常用實例
```python
s = "this is string example....wow!"
print (s.rsplit( ))
print (s.rsplit('i',1))  #從後面數來第一個i
print (s.rsplit('w'))
```
輸出：
```python
['this', 'is', 'string', 'example....wow!']
['this is str', 'ng example....wow!']
['this is string example....', 'o', '!']

```
   
#### Source
[Python中的split()函數的使用方法](https://blog.csdn.net/JohinieLi/article/details/76196882)

[Python rsplit() 方法](https://www.cnblogs.com/wushuaishuai/p/7792874.html)

[👨‍👩‍👧‍👧](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)


# Iterators
 > 疊代器

- 疊代（iteration）：重複反饋過程的活動，其目的通常是為了接近並到達所需的目標或結果
   > 每一次對過程的重複被稱為一次「疊代」\
   每一次疊代得到的結果會被用來作為下一次疊代的初始值
   >> e.g. 在python使用`for...in`進行疊代，如遍歷容器（list、tuple...）中的元素
  
在python中，可以使用內建的`hasattr()`來判斷一個物件是否是可疊代的
```python
hasattr((), '__iter__') #True

hasattr([], '__iter__') #True

hasattr({}, '__iter__') #True

hasattr(123, '__iter__') #False

hasattr('abc', '__getitem__') #True
```

也可以使用`collections.Iterable`來判斷
```python
from collections import Iterable

isinstance((), Iterable) #True

isinstance([], Iterable) #True

isinstance({}, Iterable) #True

isinstance('abc', Iterable) #True

isinstance(100, Iterable) #False
```
由此可知，dict、tuple、set和字串都是iterable  
  
  
#### iterable and iterator
  > iterator一定是iterable\
  但iterable不一定是iterator
  >> 最大差別：是否實現`__next__()`方法

在python中，所有事物都是object(物件)

- iterable：可疊代物件
   > Iter-**ables** are able to be iterated over.
   >> 可以「對其進行」疊代的物件
   
   iterable是實現`__iter__()`函式的物件（準確說是`container.__iter__()`），該函式返回的是一個iterator物件\
   （因此，iterable是可以從其獲得iterator的物件）
   1. 一個能夠一次返回**一個**元素的物件
   2. 有些iterable將包含的元素存在內存中（e.g. list），但有些不是（e.g. iterator）
      > iterable比iterator定義的範圍廣
      > - iterable：只要是能對它進行iteration的物件
      > - iterator：能夠**執行**iteration這件事的物件

- iterator：疊代器，遵循疊代協議（iterator protocol）的物件
   > Iter-**ators** are the agents that perform the iteration.
   >> 可以「執行」疊代這個活動的物件（有`__next__`函數）
   
   iterator是實現`__iter__()`和`__next__()`函式的物件（準確來說是`iterator.__iter__()`和`iterator.__next__()`）
    > 疊代協議：實現`__iter__()`與`__next__()`
    - `__iter__()`：返回iterator本身，這個物件可以呼叫`__next__`
    - `__next__()`：執行iterator的疊代行為，允許我們**顯示**地獲取**一個元素**，返回容器的下一個元素\
       實際上是執行了兩個步驟：
       1. 更新iterator狀態，令其指向後一項，以便下一次調用
       2. 返回當前結果
      
     iterator每次被調用時，會返回一個單一的值，**從而極大的節省內存資源**，這點是要特別注意的\
     ★iterator是**消耗型**的，每一個值被使用過後就消失了
     > 可以理解成用`pop`對iterator進行遍歷之後，iterator就變成一個空的容器了
     >> 但不等於None\
       若要重複使用iterator，可以利用`list()`將其結果保存
       
    使用程式碼來感受一下，使用`collections.Iterator`
    ```python
    from collections import Iterator
    
    isinstance((), Iterator) #False
    
    isinstance([], Iterator) #False
    
    isinstance({}, Iterator) #False
    
    isinstance('', Iterator) #False
    
    isinstance(123, Iterator) #False
    ```
    由此可見，tuple、list、dict雖然是iterable，但不是iterator
    
    這些iterable可以透過python內建的`iter()`獲得他們的iterator
    ```python
    from collections import Iterable, Iterator
    
    a = [1, 2, 3]
    b = iter(a)
    
    isinstance(a, Iterator) #False
    
    isinstance(b, Iterator) #True
    
    isinstance(b, Iterable) #True
    ```
    使用`next()`操作iterator
    ```python
    next(b) #1
    next(b) #2
    next(b) #3
    next(b) #StopIteration
    ```
    在iterator中每走訪一個元素，那個元素就會消失\
    當遍歷完最後一個元素後，就會出現`StopIteration`表示iterator已經空了，要停止疊代
     > 一般`for...in`在呼叫`__next__`的過程中，遇到`StopIteration`就會自動停止`for`迴圈的執行
     
     另外，對iterator進行資料類型的轉換，也會一個個對iterator中的元素做操作，所以轉換一次，iterator就空了
     ```python
     a = [1, 2, 3]
     b = iter(a)
     
     c = list(b)
     c            #[1, 2, 3]
     
     d = list(b)
     d            #[] 
     ```
     但空的iterator不等於None
     ```python
     isinstance(b, Iterator) #True
     
     if b:
       print(3)     #3
       
     if b == None:
       print(3)     # 
     ```
#### 解析`for`迴圈

python是一門講求實用主義的語言，在python中「所有的事情，都只用一個方法做到」
 > e.g.
 > - `for`：遍歷物件
 > - `while`：條件判斷

在`fot...in`中，執行了兩個動作：

- Step1. 抓取x的iterator物件，來判斷可否走訪
  > `__iter__()`

   使用`iter(x)`去抓，也就是使用`x.__iter__()`去判斷x中是否包含`__iter__()`函式（判斷x是否是iterable）
    - 如果有：就放入`iter()`函式中，回傳iterator
    - 如果沒有：`iter()`就會出現Type Error，也就表示此對象是無法被`for`迴圈走訪的

- Step2. 開始走訪iterator，取得元素
  > `__next__()`
 
   對`iter()`的回傳值調用`next()`，也就是抓取`iterator.__next__()`回傳的東西，一次次的執行，每次將回傳的值丟給i，直到遇到StopIteration例外停止
```python
for i in [1, 2, 3]:
    print(i)
```
等價於
```python
it = iter([1, 2, 3]) #得到iterator

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:        
        break
```
所以只要物件擁有`__iter__()`跟`__next__()`這兩個函式，就能被`for`使用

透視一點程式碼，此程式碼與上面執行的是一樣的
```python
it = [1, 2, 3].__iter__()

while True:
    try:
        x = it.__next__()
        print(x)
    except StopIteration:
        break
```
#### Source
[迭代器 (Iterator)迭代和可迭代](https://wiki.jikexueyuan.com/project/explore-python/Advanced-Features/iterator.html)

[Python之生成器詳解](http://kissg.me/2016/04/09/python-generator-yield/#generator)

[Python: range is not an iterator!](https://treyhunner.com/2018/02/python-range-is-not-an-iterator/)

[python 的 iterator](https://freedomknight.me/python-de-iterator/)

[暫_iterator和generator雜談之一———剖析for in內部機制](https://ithelp.ithome.com.tw/articles/10196096?sc=iThelpR)

[👨‍👨‍👦](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)

# Python: range is not an iterator!
 > `range`返回的是iterable，而非iterator

#### Source
[Python: range is not an iterator!](https://treyhunner.com/2018/02/python-range-is-not-an-iterator/)

[理解Python的Iterable和Iterator](https://www.kawabangga.com/posts/2772)

# Generator
  > 生成器
  
#### Source
[生成器](http://wiki.jikexueyuan.com/project/explore-python/Advanced-Features/generator.html)

[Python 學習筆記_20-Iterators vs Generators](https://www.youtube.com/watch?v=7UUn65QLDW0)

[Python之生成器詳解](http://kissg.me/2016/04/09/python-generator-yield/#generator)

[👨‍👨‍👧](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)

# ＿＿name＿＿
 > python中，定義class使用的一些特殊函式名稱


#### Source
[特殊方法名稱](https://openhome.cc/Gossip/Python/SpecialMethodNames.html)

# python –

#### Source
[Python，你到底是在__底線__什麼啦！](https://aji.tw/python%E4%BD%A0%E5%88%B0%E5%BA%95%E6%98%AF%E5%9C%A8__%E5%BA%95%E7%B7%9A__%E4%BB%80%E9%BA%BC%E5%95%A6/)

[👨‍👨‍👦‍👦](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)

# List Comprehension
  > 解析式列表

#### Source
[Python的列表解析式，集合解析式，字典解析式](https://blog.csdn.net/LittleHuang950620/article/details/81774402)

[👨‍👨‍👧‍👦](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)

# sort vs. sorted
 > 排序對象要屬於相同資料型態

- `list.sort(reverse=False, key=None)`
  > list內建的排序方法（限用list）
  >> 此函式會直接變動到原始的資料內容
 
- `sorted(list,  reverse=False, key=None)`
  > python內建**全域性**的排序方法（對所有可迭代序列皆有效）
  >> 此函示不會變動到原始的資料內容\
  要使用變數來儲存回傳值

不設定任何條件的話，字串會按照字母排序排列、數字則會遞增排列
  > 相反：`reverse=True`
  
#### dict sorted

- [以key排序](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#%E4%BB%A5key%E6%8E%92%E5%BA%8F)
- [以value排序](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_14#%E4%BB%A5value%E6%8E%92%E5%BA%8F)

##### 以key排序
dict內元素本身為無序，若想依照某個特定的順序來取用dict內的元素，則需要使用`for`迴圈 + `sorted()`對其進行排序

- 舉例，直接對dict執行`sorted()`
   ```python
   d = {}
   d[4] = 'four'
   d[1] = 'one'
   d[2] = 'two'
   d[5] = 'five'
   d[3] = 'three'
   d
   ```
   回傳：
   ```python
   {4: 'four', 1: 'one', 2: 'two', 5: 'five', 3: 'three'}
   ```
   使用`sorted()`排序
   ```python
   test = sorted(d)
   print(test)
   print(type(test))
   ```
   回傳：
   ```python
   [1, 2, 3, 4, 5]
   <class 'list'>
   ```
直接進行`sorted()`，只會對dict的所有`key`值作排序，而非將`key`與`value`一同排序\
因此需要搭配`for`迴圈，依照已排序好的`key`值找其對應到的`value`

   ```python
   sorted_d = dict()

   for i in sorted(d):
       sorted_d[i] = d[i]

   sorted_d
   ```
   回傳：
   ```python
   {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
   ```

##### 以value排序

使用key參數來指定排序之前要跳用的函式\
在`sorted()`函式的key參數稱為`key function`，可以自行指定排序依據的函數，當`sorted()`與`key function`搭配使用，`sorted()`會將所有要排序標的中的元素一個個丟進`key function`中，得到和標的元素一樣多的回傳值，再根據這些回傳值對原始的標的進行排序
> 因為是根據`key function`的回傳值進行排序，因此`function`的參數只能是list當中的**元素**，而不是整個list

```python
sorted(d.items(), key=lambda d: d[1])
```
> `sorted()`會對key進行排序，因此將kay轉換成其對應的value，再丟入`sorted()`

 - `items()`：存取dict當中所有的`key-value`元素
   > 回傳值為一個list，其元素皆為tuple形式的`(key, value)`
   
在此`key function`使用的是一個十分特別的function，叫作`lambda function`
 - `lambda function`：簡化的function定義方式
      - 在`lambda`後面的值：是這個function的參數
         > 在此為`d`
      - `:`後面的值：這個function的回傳值
         > 在此為`d[1]`
         >> 意思為，當這個`key function`每次拿到一個tuple作為參數，就取出index為1的值回傳

- 範例，建立dict
   ```python
   d = {}
   d['45'] = 4
   d['1'] = 1
   d['52'] = 2
   d['76'] = 5
   d['30'] = 3
   d
   ```
   回傳
   ```python
   {'45': 4, '1': 1, '52': 2, '76': 5, '30': 3}
   ```
   搭配`lambda function`對`value`進行排序
    > `sorted()`的回傳值為list，再搭配`for`迴圈的方式將其轉回dict
   ```python
   test = sorted(d.items(), key=lambda d:d[1])
   
   temp = {}
   for i in range(len(test)):
        temp[test[i][0]] = test[i][1]

   temp
   ```
   回傳
   ```python
   {'1': 1, '52': 2, '30': 3, '45': 4, '76': 5}
   ```

#### Source
[Python 初學第十講 — 排序](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-f3148ebb33a4)

[Python 初學第六講 — 串列的更多操作](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-f1b4e7d2e5ac)

[python sort、sorted高階排序技巧](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/373191/)

[排序指南](https://docs.python.org/zh-cn/3/howto/sorting.html)

[👨‍👩‍👦](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)


# key vs. value

#### Source
[Python基礎——字典中由value查key的幾點說明](https://blog.csdn.net/ywx1832990/article/details/79145576)

[👨‍👩‍👦‍👦](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)


# Greedy Algorithm
 > 貪婪演算法、貪心演算法
 >> 尋找「最佳解」的方法
 
 尋找方法：在每一步選擇中都採取**當前看起來最好的選擇**，進而希望最終答案是**最佳的**方法
  > 不斷的改進解答，直到無法改進為止
  
 使用此演算法的前提是，必須確保局部最佳解能解決全域最佳解
  > 簡單的說，問題能夠分解為子問題來解決，子問題的最佳解能遞推到最終問題的最佳解
  
 可以解決一些最佳化問題，但一般無法得到理想中的答案（沒有測試所有可能的解，容易**過早做決定**，因而無法達到最佳解）
  > 可解決e.g. Minimal Spanning Tree、Huffman Coding（哈夫曼編碼）...
  >> 一個問題如果可以通過greedy algorithm來解決，那通常greedy algorithm是解決此問題的最好辦法
 

#### Source
[貪婪演算法](https://zh.wikipedia.org/wiki/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95)

[貪婪演算法(Greedy)](https://www.csie.ntu.edu.tw/~b98902112/cpp_and_algo/cpp02/greedy.html)

[貪婪式演算法的原理](http://ccckmit.wikidot.com/so:greedyalgorithm)

[👪](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)


# Disjoint Sets
 > 互斥集合、併查集\
 又稱為union-find資料結構、merge-find資料結構
 >> 資料結構：檢查一個graph是否存在一個cycle
 
 一堆集合中，各自擁有的元素都各不相同，也就是集合與集合之間彼此沒有交集
 
- union-find：給出n個vertex，vertex與vertex之間要麼連通要麼不連通，此為實現連通函數（union）以及判斷vertex之間是否為直接連通或間接連通（connected）的函數
  > disjoint sets的合併及查詢
 
功能：
 - union：將兩個set做聯集，合併成一個set
 - find：尋找一個元素是在哪個set
 - split：將一個set拆成兩個set
 
#### 操作
將edge連接的vertex放到同一個set裡面，若連接的vertex已存在別的set中，則將兩個set合併
 > 同一個set：站在任一個vertex上，都可以走到相同set的任意一個vertex
 >> 若選中的edge其連接的vertex已存在同一個set中，即會出現cycle

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/image/Snipaste_2019-12-24_16-22-02.png)

使用一個array，紀錄每個vertex的parent\
每個vertex先預設為-1
> -1：獨立的vertex

在同一個set中，找一個vertex A作為parent，並將相同set的其他vertex其parent更改為A\
當合併兩個set時，將其parent改為相同即可\
當edge連接的vertex已有相同的parent時，代表採用此edge即會出現cycle

#### Source
[Disjoint Sets](http://www.csie.ntnu.edu.tw/~u91029/Set.html#5)

[1042 Quiz#1 互斥集合 (Disjoint Sets)](http://squall.cs.ntou.edu.tw/cpp/1042/labtest/test1/DisjointSets.html)

[并查集（Disjoint-set union）第1讲](https://www.youtube.com/watch?v=YKE4Vd1ysPI)

[普林斯頓課程學習筆記1 Union-find](https://medium.com/@gxyou45/algorithm%E6%99%AE%E6%9E%97%E6%96%AF%E9%A0%93%E8%AA%B2%E7%A8%8B%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%981-union-find-5af7911ca5ef)

[👨‍👩‍👧](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)

# Minimum Spanning Tree
 > 最小生成樹：關心**邊**的問題
 >> 此為Kruskal's Algorithm：採Greedy Algorithm
 
 - [Spanning Tree](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#-spanning-tree-)
 - [Practice](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#-practice-)
 - [Exercise](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#-exercise-)
 - [Kruskal's Algorithm](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#-kruskals-algorithm-)
 - [Time Complexity](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#-time-complexity-)

將複雜問題簡化到graph的問題上，讓graph的edge數字，可以代表某種cost（可將所有可能情形疊加在graph）
 > e.g.花費時間、花費金額...
 
 建立最佳選擇之前，要有一個lower burden（最低負擔）的評估模式\
 以最小的cost走訪完每個vertex

- Minimum Spanning Tree：將複雜問題映射到圖論的問題上，並將最低的花費、成本考量進來
  > 可保留minimum cost，進而規劃後面的資源
  
minimum spanning tree（最小生成樹）有很多實際應用\
將node看作城市，edge看作連線城市的通訊網，edge的weight看作連線城市通訊線路的成本，根據minimum spanning tree建立的通訊網就是這些城市之間成本最低的通訊網



#### § Spanning Tree §

- Spanning Tree：在graph中，可以找到一個tree視為graph的subset（此tree包含graph的所有vertex）
   - 有兩個關鍵，因為是tree：
       1. 不可有loop
       2. 所有node，任兩點一定可以找到path走到對方（完全連通）
          > node不可有isolated（孤立）的情況
          >> 若graph並非完全連通，則沒有spanning tree，而是擁有許多棵spanning sub-tree（生成子樹）構成的spanning forest（生成森林）
          
建立minimum spanning tree有兩個判斷條件：
 > 方式：**邊的個數 = 點-1**
 >> 邊的個數也可作為停止的條件
1. 是否有cycle
2. 是否為連通的tree

可以想像成許多的MST做作union（聯集）
 > 用disjoint set作為union-find之輔助
1. root不同即可union
2. root相同不可union
   > 會出現cycle

#### § Practice §
 > min cost會唯一

edge有weight（權重），其對應的是cost

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/MST_kruskal_en.gif/255px-MST_kruskal_en.gif)

1. 先將cost排序，**由小排到大**，從小的開始，再使用disjoint sets（互斥集、併查集）來作紀錄
2. parent的紀錄先設為 -1，當有edge加入時，再將-1更改為起點，並記錄cost
   > -1：代表尚未走訪過 
3. 按照sorted順序慢慢加入，方向性先固定，左邊是起點右邊是終點，當邊數滿足即可停止
   > 假設左邊為右邊的root
   >> 會產生loop的edge就不放入
4. 最後吐出graph min cost的路徑與minimum cost

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/image/Snipaste_2019-12-24_16-22-02.png)
 > 此為記錄parent，edge增加parent就可能要update
 >> 紀錄可採linked list的方式（如圖），方便查詢即可
 
☆ 將兩個disjoint set合併時，要決定誰要當root
  > 先確定一個方向（src當parent還是dest當parent），置換或合併時採相同的動作


#### § Exercise §
 > 儲存紀錄對象：edge

- 畫圖表示，無使用edge表紀錄採用的edge與其cost

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/image/MST.gif)


- 畫圖表示，並且使用edge表紀錄採用的edge與其cost

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/image/output_UjbChm.gif)


#### § Kruskal's Algorithm §
 > 解決如何生成一個「最小生成樹」的問題
 >> 是處理minimum spanning tree最經典的一個作法
 
需要決定的是「tree產生了沒」，需要在意的是：
1. There is no cycle.
   > disjoint set不斷在看，是否有cycle發生
2. The graph is connected.
   > 兩個方法：
   > 1. 觀察edge是否達到v-1的數量
   > 2. 建tree時，呼叫BFS/DFS走訪（若連通，即可走完每個點）
   
#### § Time Complexity §
 > O(E log E)或O(E log V)

- 前面的E：要先排序edge，所以會先走訪完全部的邊

- 後面的E/V： E = V-1（1過小可忽略），所以E = V
- log：每走訪一個E/V次數是隨log指數減少的
 
 #### Source
 [維基百科_克魯斯克爾演算法](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95)
 
 [Kruskal’s Minimum Spanning Tree Algorithm | Greedy Algo-2](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/)
 
 [[101北一資訊集訓] 06_3_1 MST之Kruskal演算法(NEW)](https://www.youtube.com/watch?v=wuU4DDEUu1w)

[Kruskal's algorithm in 2 minutes — Review and example](https://www.youtube.com/watch?v=71UQH7Pr9kU&feature=emb_logo)

[Check if a given graph is tree or not](https://www.geeksforgeeks.org/check-given-graph-tree/)

[Detect cycle in an undirected graph](https://www.geeksforgeeks.org/detect-cycle-undirected-graph/)

[Spanning Tree](http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html)

[👨‍👩‍👧‍👦](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)


# Adjustment of Design Kruskal
  > 調整作業六Kruskal程式碼
  
[👉🏽HERE👈🏽](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14/Adjustment%20of%20Design%20Kruskal.py)

增加計算min cost的值\
在Kruskal中，tree可能不唯一（依據鄰邊表的排序變動會有差異），但min cost一定會唯一

- 回傳：min_cost, MST

[👨‍👨‍👧‍👧](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_14#content)
