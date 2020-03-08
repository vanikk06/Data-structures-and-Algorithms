# Content
- [import](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#import)
- [Magic Methods](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#magic-methods)
- [Ipython](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#ipython)
- [Technical Term](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#technical-term)
- [Docker](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#docker)
  - [Hypervisor](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#hypervisor)



# import

#### Source
[Python import 簡易教學](https://medium.com/@alan81920/python-import-%E7%B0%A1%E6%98%93%E6%95%99%E5%AD%B8-c98e8e2553d3)

[Python 的 Import 陷阱](https://medium.com/pyladies-taiwan/python-%E7%9A%84-import-%E9%99%B7%E9%98%B1-3538e74f57e3)

[Python Tutorial 第二堂（3）函式、模組、類別與套件](http://www.codedata.com.tw/python/python-tutorial-the-2nd-class-3-function-module-class-package)

[🛹](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#content)

# Magic Methods
  > 魔法方法



#### Source
[Python - Magic Methods](https://www.tutorialsteacher.com/python/magic-methods-in-python)

[11. (译)Python魔法方法指南](https://pyzh.readthedocs.io/en/latest/python-magic-methods-guide.html)

[Python魔術方法指南](https://pycoders-weekly-chinese.readthedocs.io/en/latest/issue6/a-guide-to-pythons-magic-methods.html)

[Python魔法方法總結及注意事項](https://www.cnblogs.com/Jimmy1988/p/6801795.html)

[🚲](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#content)



# Ipython
  > Ipython與Jupyter Notebook是強大的**互動式開發環境**
  
  
- Ipython：一個提供互動運算的命令界面（command shell）
  > 以命令列的方式操作和互動
  >> 與Python IDLE相似，皆為python直譯器（Interpreter）：都會立即執行並輸出結果

  IPython提供強大功能的神奇函數(Magic functions)，還能執行作業系統命令

  優點
  - 提供強大功能的程式互動界面
  - 整合不同編輯器，並執行作業系統命令
  - 視覺化的運算資料呈現，並結合圖形化工具
  - Python程式專案管理
  - 支持平行運算
  - 並且是Jupyter Notebook的核心
    > Jupyter Notebook原名為IPython Notebook

- Jupyter Notebook：可以想像成IPython + Notebook

  包含：
   - The notebook web application
   - Kernels：前面的IPython，是Jupyter Notebook的核心
   - Notebook documents：開放原始碼的web開發環境

  特別地方在於，可以將程式開發的過程連同程式碼、數學公式、說明文字、圖示、運算結果，甚至是影片都完整的紀錄，還可以重複編輯、修改和執行
  
  套件：
  - `IPython.display Math`：可以製作漂亮的數學公式
     ```python
     from IPython.display import Math
     ```
  - `IPython.display Image`、`IPython.display HTML`、`IPython.lib.display YouTubeVideo`：多媒體呈現，可以顯示圖片、HTML，甚至是YouTube影片
    ```python
    from IPython.display import Image #圖片
    
    from IPython.display import HTML  #HTML
    
    from IPython.lib.display import YouTubeVideo #YouTube影片
    ```

#### Source
[學習 Python 不可不知的開發工具 IPython 和 Jupyter Notebook](http://seansharingblog.blogspot.com/2017/09/python-ipython-jupyter-notebook.html)

[🛴](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#content)

# Technical Term
  > 專有名詞


[🛵](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#content)

# Docker
  > 一種核心層級的虛擬化技術
  >> Container（容器）：在作業系統層級的虛擬化技術
 
Docker 是一個開源專案，是基於 Google 公司推出的 Go 語言實作

![](https://miro.medium.com/max/504/0*7pLYtIrRNXSsER2M.png)
 
 - [虛擬化技術](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#-%E8%99%9B%E6%93%AC%E5%8C%96%E6%8A%80%E8%A1%93-)
    - [虛擬機器](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#%E8%99%9B%E6%93%AC%E6%A9%9F%E5%99%A8)
    - [容器](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#%E5%AE%B9%E5%99%A8)
 - [Docker 三元素](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#-docker-%E4%B8%89%E5%85%83%E7%B4%A0-)
    - [映像檔](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#%E6%98%A0%E5%83%8F%E6%AA%94)
    - [容器](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#%E5%AE%B9%E5%99%A8-1)
    - [倉庫](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#%E5%80%89%E5%BA%AB)
 - [Docker 實例]()
 
 
【Docker解決之問題】\
改善傳統虛擬機器，因為需要額外安裝作業系統（Guest OS），導致啟動慢、佔較大記憶體的問題

【Docker提供之解決方法】\
以「應用程式」為核心虛擬化，取代傳統需要 Guest OS 的虛擬化技術

- Operating System（OS）：作業系統，主要為管理、協調電腦硬體資源，使硬體資源可以正確無誤的完成使用者所下達的各種指令，同時確保整個電腦可以在一個穩定的狀況下提供服務

[Learning more](https://philipzheng.gitbooks.io/docker_practice/content/)

P.S. 不適用於 Windows家用版（[安裝參考](https://www.itread01.com/content/1545817893.html)）

### § 虛擬化技術 §

【虛擬化解決之問題】- 程式執行的環境問題\
每台電腦的作業系統與硬體配置不盡相同，我的程式可能剛好只跟我的電腦上的環境相容

虛擬化要做的就是「模擬出一個環境」，讓程式可以在不同硬體上執行時，都以為自己在同一個環境中執行

- 常見的虛擬化技術：
  - [虛擬機器（Virtual machine）](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#%E8%99%9B%E6%93%AC%E6%A9%9F%E5%99%A8)：在**系統層級**的虛擬化技術   e.g. Virtual Box
    > 以「作業系統」為中心
    
  - [容器（Container）](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#%E5%AE%B9%E5%99%A8)：在**作業系統層級**的虛擬化技術  e.g. Docker
    > 以「應用程式」為中心

#### 〔虛擬機器〕

目標：將一個應用程式所需的執行環境打包起來，建立一個**獨立環境**，方便在不同的硬體中移動

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/Something/image/Snipaste_2020-03-07_18-25-25.png)

Virtual machine是在系統層上的虛擬化，透過 Hypervisor 在目標的機器上，提供可以執行一個或多個虛擬機器的平台。\
這些Virtual machine，可以執行完整的作業系統。

- Hypervisor：一個可以讓電腦在原本的作業系統（Host OS）上，再裝一個作業系統（Guest OS），且兩個作業系統彼此不會打架的平台
  > [Learning more](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#hypervisor)

透過選擇不同的 Guest OS ，Virtual machine的技術就可以確保，只要我的程式在 Guest OS 可以正常運作，那放到你的電腦時可以不管你的 Host OS 是什麼，只要你的 Host OS 上先裝上我的 Guest OS ，我的程式就可以在你的電腦上正常運作。

#### 〔容器〕

目標：改善Virtual machine因為需要安裝 Guest OS 導致啟動慢、佔較大記憶體的問題

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/Something/image/Snipaste_2020-03-07_18-28-51.png)

Container是在作業系統層上的虛擬化，透過 Container Manager 直接將一個應用程式所需要的程式碼、函式庫**打包**，建立資源控管機制隔離各個容器，並**分配 Host OS 上的系統資源**。\
透過 Container，應用程式不需要再另外安裝作業系統（Guest OS）也可以執行。

因不需另外安裝作業系統，建立 Container 所需要的硬碟容量可以大幅降低，且啟動速度可以更快，不用等待 Guest OS 的開機時間。

### § Docker 三元素 §

使用 Docker 時最重要的三個元素：
- 映像檔（Image）：可以用來建立 Docker Container
  > 唯讀（read-only）的模板
- 容器（Container）：Container 是從 Image 建立的**執行實例**，Docker利用 Container 來執行應用
- 倉庫（Repository）：集中存放 Image 檔案的場所

以一個簡單的比喻解釋\
如果 Image 是一個做蛋糕用的「模具」，Container 則是「用模具烤出來的蛋糕」，而 Repository 是用來集中放置模具們的「收納櫃」。

#### 〔映像檔〕
Docker Image 是一個**唯讀的模板**，用來重複產生 Container 實體。
> e.g. 一個 Image 可以包含一個完整的 MySQL 服務、一個 Golang 的編譯環境、一個 Ubuntu 作業系統...等

透過 Docker Image 我們可以快速的產生可以執行應用程式的 Container，而 Docker Image 可以透過撰寫命令行構成的 Dockerfile 輕鬆建立，也可以從公開的地方下載別人已經作好的 Image 來使用。
> Dockerfile：透過撰寫命令行告訴 Docker 應該如何打包我的程式

※ P.S.
- Golang：又稱 Go語言，是 Google 開發的一種靜態強型別通用編譯語言
  
  ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/Something/image/Snipaste_2020-03-07_21-35-38.png)
  
  - [特性介紹](https://michaelchen.tech/golang-programming/why-or-why-not-golang/)
  - [語法介紹](https://yami.io/php-to-golang/#%E8%BC%B8%E5%87%BAecho)

- Ubuntu：是流行的 Linux 發行版
  
#### 〔容器〕
Container 是由 Image 建立出來的**執行實例**，可以被啟動、開始、停止、刪除，每個 Container 都是相互隔離、保證安全的平台。

可以把 Container 看作是一個簡易版的 Linux 環境（包括root使用者權限、程式空間、使用者空間、網路空間...等等）和在其中執行的應用程式。

另外需要注意的是，Docker Image 是唯讀的，而 Container 在啟動時會建立一層可以被修改的「可寫層」作為最上層，讓 Container 的功能可以再被擴充。

#### 〔倉庫〕
Repository 是集中存放 Image 檔案的場所，與 Registry 不完全相同，可分為公開（Public）和私有（Private）兩種形式。

- Registry：倉庫註冊伺服器，在 Registry 上存放著多個 Repository
  > 最大的公開倉庫註冊伺服器：[Docker Hub](https://hub.docker.com/)
- Repository：倉庫，每個 Repository 中包含了多個 Image，而每個 Image 有不同的標籤（tag）

Docker Repository的概念與 Git 類似，Registry 可以理解為 GitHub 這樣的託管服務。\
使用者建立自己的 Image 之後，可以使用`push`命令將其上傳到公有或私有 Repository，當下次在另外一台機器上使用這個 Image 時，只需要從 Repository 上`pull`下來即可。

#### Docker 實例

- Dockerize：將應用程式所需要的程式碼、套件**打包**成 Docker Image

理論上，一個 Image 裡可以放多個程式與服務，但 Docker 團隊建議，一個 Image 裡面只裝一個一個程式，再把 Image 一層層疊起來，以提供一個完整的服務，也就是 Docker 的「Image 堆疊概念」

- Image堆疊

  Image本身是唯讀的，因此當我們要在 Image 上再疊一層時，需要先將它建立成 Container 實體，然後運用 Container 啟動時會在最上面建造可寫層的特性。\
  我們就可以在 Container 裡面透過另一個 Image 建立 Container 實體，最後再將 Container 疊上 Container 的實體轉成 Image，就完成了 Image 堆疊
  
  【範例】
   做出一個 Docker Image，執行網頁與其後端伺服器。\
   假設我們需要 Alpine OS、Apache Server、MySQL Database，要如何把他們疊起來呢？
   
   - 釐清：Why Docker 裡面還需要一個作業系統？
      
     在 Container 的世界裡，這個作業系統稱之為 Base OS。\
     我們可以將它想像成一個「超級精簡版的OS」，因為 Container 是使用 Host OS 上的 Kernel（核心），所以這個 Base OS 就只要裝最必要的一些執行檔。
   
   首先，先從 DockerHub 上下載 Alpine Image，用 Docker 執行 Image 產生 Container 後，在產生出的 Container 內再安裝 Apache，等安裝完成後把整個 Container 打包成另一個新的 Image。\
   繼續反覆這樣的程序，從 Alpine-Apache 建立的 Image 透過 Docker 產生新的 Container，在新的 Container 裡面安裝下一層的 MySQL，然後再將整個 Container 打包，我們就得到一個含有 Alpine、Apache、MySQL 的 Image 了！

此外，[Docker Compose](https://blog.techbridge.cc/2018/09/07/docker-compose-tutorial-intro/)也是非常值得學習的工具

※ P.S.
- Alpine OS：一個 Linux 的發行版，以「安全」為理念而設計的作業系統
- Apache Server：一個開放原始碼的網頁伺服器軟體，是最流行的 Web伺服器軟體之一
  - 網頁伺服器（Web Server）有三個意思
    > [Learning more](https://www.newscan.com.tw/all-knowledge/knowledge-detail-6.htm)
    - 一台提供服務的電腦
    - 一台負責提供網頁的電腦，主要是HTML檔案，透過HTTP協定傳給客戶端（一般是指網頁瀏覽器）
      > HTTP：HyperText Transfer Protocol，超文本傳輸協定，是一種用於分佈式、協作式和超媒體訊息系統的應用層協定
    - 一個提供網頁的伺服器程式
  

#### Source
[Docker 基礎教學與介紹 101](https://medium.com/unorthodox-paranoid/docker-tutorial-101-c3808b899ac6)

[Docker —— 從入門到實踐](https://philipzheng.gitbooks.io/docker_practice/content/)

[最新Docker的安裝與使用以及常見問題 Linux Windows 2018-12-26](https://www.itread01.com/content/1545817893.html)

[Docker Compose 建置 Web service 起步走入門教學](https://blog.techbridge.cc/2018/09/07/docker-compose-tutorial-intro/)

[維基百科_Go](https://zh.wikipedia.org/wiki/Go)

[[Golang] 程式設計教學：為什麼用 (或不用) Golang](https://michaelchen.tech/golang-programming/why-or-why-not-golang/)

[從 PHP 到 Golang 的筆記](https://yami.io/php-to-golang/#%E8%BC%B8%E5%87%BAecho)

[維基百科_Alpine Linux](https://zh.wikipedia.org/wiki/Alpine_Linux)

[維基百科_Apache HTTP伺服器](https://zh.wikipedia.org/wiki/Apache_HTTP_Server)

[網頁伺服器（Web Server）是什麼?](https://www.newscan.com.tw/all-knowledge/knowledge-detail-6.htm)

[🏍](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#content)

## Hypervisor
  > 又稱「虛擬機監視器」（Virtual Machine Monitor，VMM）

Hypervisor 是一種運行在「物理伺服器」和「作業系統」之間的**中間軟體層**，是所有虛擬化技術的核心。

- 字面含義：Hypervisor，n.超級監督者，引申為超級管理程式、超多功能管理器、虛擬機管理器、VMM
  > super、hyper為同義詞，皆為「超級」的意思


允許多個作業系統和套件共享一套基礎物理硬體，也可以視作一種虛擬環境中的「元」作業系統，它可以協調訪問伺服器上的所有物理設備（包括磁碟、記憶體...等等），也同時在各個虛擬機之間施加防護。
當伺服器啟動並執行 Hypervisor 時，它會載入所有虛擬機客戶端的作業系統，同時會分配給每一台虛擬機適當的記憶體、CPU、網路和磁碟。

- 依照 Hypervisor 安裝位置可分為兩類：
  - Type Ⅰ：又稱為 bare-metal hypervisor（與"裸機"裝虛擬機有關）
      
      是直接裝一層 hyperviosr 在空機上面，然後將VM（Virtual Machine）的系統安裝在 hypervisor，如此的虛擬系統離硬體控制較近，VM要控制的硬體資源會**直接透過 hypervisor 去操作**
  - Type Ⅱ：又稱為 hosted hypervisor
  
      與 Type Ⅰ 相反，必須先安裝作業系統之後再去安裝 hypervisor，這類的 hypervisor 的硬體控制方式是透過**原本的作業系統代為處理**

#### Source
[hypervisor](https://www.itsfun.com.tw/Hypervisor/wiki-5555507-8928386)

[初探虛擬機和虛擬化](https://freedomknight.me/chu-tan-xu-ni-ji-he-xu-ni-hua/)

[What is a Hypervisor?](https://www.youtube.com/watch?v=VtXNIy_noWg)

[🏍🏍](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#content)
