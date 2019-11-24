# Content
- [Code](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#code)
   - [Insert](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#insert)
   - [Search](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#search)
   - [Delete](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#delete)
   - [Modify](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#modify)
  
  
- [Jupyter notebook_The process of learning binary search tree](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/The%20process%20of%20learning%20binary%20search%20tree%20.ipynb)
    - [Jupyter nbviewer_The process of learning binary search tree](https://nbviewer.jupyter.org/github/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/The%20process%20of%20learning%20binary%20search%20tree%20.ipynb)

- [Jupyter notebook_Binary Search Tree功能說明](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/Binary%20Search%20Tree%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E.ipynb)
    - [Jupyter nbviewer_Binary Search Tree功能說明](https://nbviewer.jupyter.org/github/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/Binary%20Search%20Tree%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E.ipynb)


# Code
[🤜🏼HERE🤛🏼](https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_09/H.W.3_Binary%20Search%20Tree/Binary%20Search%20Tree.py)

此次作業構思方式是採將現階段概念理解的內容，嘗試依造自己的想法逐步轉為執行步驟，過程再根據遇到的問題去進行調整、修正，直到測資結果符合預期

- 作業規則：
   1. 在已存在BST上，執行下列功能
   2. 回傳值為class
   3.
   

- 反思：

   一開始思考的不夠完備，不是找到一般化的處理方式才開始打code，而是在過程將遇到的問題做出調整；解決的也僅有此次側資遇到的問題，若變換測資，不一定能達到預期效果（仍存在Bug）
   
   - 缺：
        1. 程式碼過長：判斷繁雜，排除目前問題方式採增加判斷式
            > BST向下增加一層，其可能結果是2的**指數成長**
        2. 考慮不夠完備：思考到的處理方式，無法涵蓋到所有可能範圍
        3. 時間不夠充分：在打這次作業的時候，剛好事情比較多，無妥善分攤導致作業製作的時間緊迫

## Insert
   > 新增、插入
   
   增加的val必須與root（parent）比較，大的放right，小的放left，若其位置已有node存在，就繼續往下一層放
   
### Code
   > 採**遞迴**，執行重複的判斷動作
   
   - root是否存在
   
   
[🔸](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#content)

## Search
   > 搜尋、走訪
   
   
[🔹](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#content)

## Delete
   > 刪除

[🔶](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#content)

## Modify
   > 修改

[🔷](https://github.com/vanikk06/Data-structures-and-Algorithms/tree/master/week_09/H.W.3_Binary%20Search%20Tree#content)
