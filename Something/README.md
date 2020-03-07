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
 
 ![](https://miro.medium.com/max/504/0*7pLYtIrRNXSsER2M.png)
 
 - []()
    - []()
    - []()
 - []()
 
【Docker解決之問題】\
改善傳統虛擬機器，因為需要額外安裝作業系統（Guest OS），導致啟動慢、佔較大記憶體的問題

【Docker提供之解決方法】\
以「應用程式」為核心虛擬化，取代傳統需要 Guest OS 的虛擬化技術

- Operating System（OS）：作業系統，主要為管理、協調電腦硬體資源，使硬體資源可以正確無誤的完成使用者所下達的各種指令，同時確保整個電腦可以在一個穩定的狀況下提供服務

[Learning more](https://philipzheng.gitbooks.io/docker_practice/content/)

#### § 虛擬化技術 §

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
  > [Learning more]()

透過選擇不同的 Guest OS ，Virtual machine的技術就可以確保，只要我的程式在 Guest OS 可以正常運作，那放到你的電腦時可以不管你的 Host OS 是什麼，只要你的 Host OS 上先裝上我的 Guest OS ，我的程式就可以在你的電腦上正常運作

#### 〔容器〕

目標：改善Virtual machine因為需要安裝 Guest OS 導致啟動慢、佔較大記憶體的問題

![](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/Something/image/Snipaste_2020-03-07_18-28-51.png)

Container是在作業系統層上的虛擬化，透過 Container Manager 直接將一個應用程式所需要的程式碼、函式庫**打包**，建立資源控管機制隔離各個容器，並**分配 Host OS 上的系統資源**\
透過 Container，應用程式不需要再另外安裝作業系統（Guest OS）也可以執行

因不需另外安裝作業系統，建立 Container 所需要的硬碟容量可以大幅降低，且啟動速度可以更快，不用等待 Guest OS 的開機時間

#### § Docker 三元素 §

使用 Docker 時最重要的三個元素：
- 映像檔（Image）：可以用來建立 Docker Container
  > 唯讀（read-only）的模板
- 容器（Container）：Container 是從 Image 建立的**執行實例**，Docker利用 Container 來執行應用
- 倉庫（Repository）：集中存放 Image 檔案的場所

以一個簡單的比喻解釋\
如果 Image 是一個做蛋糕用的「模具」，Container 則是「用模具烤出來的蛋糕」，而 Repository 是用來集中放置模具們的「收納櫃」

#### 〔映像檔〕
#### 〔容器〕
#### 〔倉庫〕

#### Source
[Docker 基礎教學與介紹 101](https://medium.com/unorthodox-paranoid/docker-tutorial-101-c3808b899ac6)

[Docker —— 從入門到實踐](https://philipzheng.gitbooks.io/docker_practice/content/)

[🏍](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#content)

## Hypervisor
  > 


#### Source

[🏍🏍](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/Something#content)
