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

Virtual machine是在系統層上的虛擬化，透過 Hypervisor 在目標的機器上，提供可以執行一個或多個虛擬機器的平台\
這些Virtual machine，可以執行完整的作業系統

- Hypervisor：一個可以讓電腦在原本的作業系統（Host OS）上，再裝一個作業系統（Guest OS），且兩個作業系統彼此不會打架的平台
  > [Learning more](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#hypervisor)

透過選擇不同的 Guest OS ，Virtual machine的技術就可以確保，只要我的程式在 Guest OS 可以正常運作，那放到你的電腦時可以不管你的 Host OS 是什麼，只要你的 Host OS 上先裝上我的 Guest OS ，我的程式就可以在你的電腦上正常運作

#### 〔容器〕

目標：改善Virtual machine因為需要安裝 Guest OS 導致啟動慢、佔較大記憶體的問題

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/Something/image/Snipaste_2020-03-07_18-28-51.png)

Container是在作業系統層上的虛擬化，透過 Container Manager 直接將一個應用程式所需要的程式碼、函式庫**打包**，建立資源控管機制隔離各個容器，並**分配 Host OS 上的系統資源**\
透過 Container，應用程式不需要再另外安裝作業系統（Guest OS）也可以執行

因不需另外安裝作業系統，建立 Container 所需要的硬碟容量可以大幅降低，且啟動速度可以更快，不用等待 Guest OS 的開機時間

### § Docker 三元素 §

使用 Docker 時最重要的三個元素：
- 映像檔（Image）：可以用來建立 Docker Container
  > 唯讀（read-only）的模板
- 容器（Container）：Container 是從 Image 建立的**執行實例**，Docker利用 Container 來執行應用
- 倉庫（Repository）：集中存放 Image 檔案的場所

以一個簡單的比喻解釋\
如果 Image 是一個做蛋糕用的「模具」，Container 則是「用模具烤出來的蛋糕」，而 Repository 是用來集中放置模具們的「收納櫃」

#### 〔映像檔〕
Docker Image 是一個**唯讀的模板**，用來重複產生 Container 實體
> e.g. 一個 Image 可以包含一個完整的 MySQL 服務、一個 Golang 的編譯環境、一個 Ubuntu 作業系統...等

透過 Docker Image 我們可以快速的產生可以執行應用程式的 Container，而 Docker Image 可以透過撰寫命令行構成的 Dockerfile 輕鬆建立，也可以從公開的地方下載別人已經作好的 Image 來使用

※ P.S.
- Golang：又稱 Go語言，是 Google 開發的一種靜態強型別通用編譯語言
  
  ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/Something/image/Snipaste_2020-03-07_21-35-38.png)
  ![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/Something/image/Snipaste_2020-03-07_21-28-57.png)
  
  - [特性介紹](https://michaelchen.tech/golang-programming/why-or-why-not-golang/)
  - [語法介紹](https://yami.io/php-to-golang/#%E8%BC%B8%E5%87%BAecho)

- Ubuntu：是流行的 Linux 發行版
  
  ![](data:image/png;base64,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)


#### 〔容器〕
Container 是由 Image 建立出來的**執行實例**，可以被啟動、開始、停止、刪除，每個 Container 都是相互隔離、保證安全的平台

可以把 Container 看作是一個簡易版的 Linux 環境（包括root使用者權限、程式空間、使用者空間、網路空間...等等）和在其中執行的應用程式


#### 〔倉庫〕

#### Source
[Docker 基礎教學與介紹 101](https://medium.com/unorthodox-paranoid/docker-tutorial-101-c3808b899ac6)

[Docker —— 從入門到實踐](https://philipzheng.gitbooks.io/docker_practice/content/)

[最新Docker的安裝與使用以及常見問題 Linux Windows 2018-12-26](https://www.itread01.com/content/1545817893.html)

[維基百科_Go](https://zh.wikipedia.org/wiki/Go)

[[Golang] 程式設計教學：為什麼用 (或不用) Golang](https://michaelchen.tech/golang-programming/why-or-why-not-golang/)

[從 PHP 到 Golang 的筆記](https://yami.io/php-to-golang/#%E8%BC%B8%E5%87%BAecho)

[🏍](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#content)

## Hypervisor
  > 


#### Source

[🏍🏍](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#content)
