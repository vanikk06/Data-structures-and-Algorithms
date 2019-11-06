class Solution(object):
    
    def _divide(self, list, n:int):
        """
        分堆
        """
        if n <= 1:                           #迴圈出口：如果長度<=1就跳出
            return list
                                             #分成兩堆
        left = []                              #左邊
        right = []                             #右邊
    
        n1 = int(n/2)                        #左邊長度
        n2 = n - n1                          #右邊長度
    
        for i in range(n1):                  #將list的值放入左邊堆
            left.append(list[i])
    
        for j in range(n1, n):               #將list的值放入右邊堆
            right.append(list[j])
           
        left = self._divide(left, n1)        #遞迴繼續分堆
        right = self._divide(right, n2)
    
        return self._merge(left, right)      #回傳合併後的結果
    
    
    def _merge(self, left, right):
        """
        合併
        """
    
        temp = []                           #創造一個合併後空間
    
        n1 = len(left)                      #左邊堆長度
        n2 = len(right)                     #右邊堆長度
    
        i = 0
        j = 0
        while i < n1 and j < n2:            #將左右堆一個個比較，按小到大順序合併
            if left[i] < right[j]:
                temp.append(left[i])
                i += 1
            else:
                temp.append(right[j])
                j += 1
    
        if i == n1:                         #如果左邊堆比完，把右邊堆剩下的值一個個放入
            while j < n2:
                temp.append(right[j])
                j += 1
        else:
            while i < n1:                   #如果右邊堆比完，把左邊堆剩下的值一個個放入
                temp.append(left[i])
                i += 1
    
        return temp                         #回傳合併結果
    
    def merge_sort(self, list):
        """
        進行merge sort
        """
        n = len(list)
        return self._divide(list, n)
