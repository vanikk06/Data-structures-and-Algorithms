不要有loop：邊=點-1

# 黑板
-1：還沒走訪過
加入edge將-1更改為連結對象，並記錄cost
 > be加入會有loop產生
 
 > 邊滿足即可停止


# Minimum Spanning Tree
 > 最小生成樹：關心**邊**的問題
 >> Kruskal's Algorithm

將複雜問題簡化為graph的問題，讓graph上的edge數字，可以代表某種cost（可將所有可能情形疊加在graph上）
 > e.g.花費時間、花費金額...
 
 建立最佳選擇之前，要有一個lower burden（最低負擔）的評估模式
