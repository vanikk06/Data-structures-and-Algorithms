class Solution(object):
   
    def _heapity(self, list, n:int, i:int):
        """
        架構heap
        """
       

        if i >= n:                                    #當新parents的index超過list長度就不須再往下檢查
            return                                      #等於list長度也不需要，因其必為child
                                                      #index
        Min = i                                         #最初放入的index為i,暫定為Min(parents)
        left = 2*i+1                                    #parents與左邊child關係
        right = 2*i+2                                   #parents與右邊child關係
    
        if left < n and list[Min] > list[left]:       #parents與左邊child比較
            Min = left                                #若left在list長度內，且其值小於Min，則取代Min
    
        if right < n and list[Min] > list[right]:     #parents與右邊child比較
            Min = right                               #若right在list長度內，且其值小於Min，則取代Min
        
        if Min == left or Min == right:                                  #若Min發生改變
            list[i], list[Min] = list[Min], list[i]   #則將i(parents)的值與Min的值交換
        
            self._heapity(list, n, Min)                     #以新的parents繼續往下檢查
        
        
    

    def _build_minheap(self, list, n:int):
        """
        由下往上進行heapity
        """
        last = n-1                          #最後一個node
        parents = (last-1)//2               #child與parents的關係，取整數位
        for i in range(parents, -1, -1):    #由後往前一個個進行heapity並往上堆疊
            self._heapity(list, n, i)
            
    
    

    def heap_sort(self, list):
        """
        以minheap進行heap sort
        """
        n = len(list)                  #list長度(node個數)    
    
        self._build_minheap(list, n)        #建立minheap
    
        for i in range(1,n+1):              #將balance的min抽出，再re-balance
            list.append(list.pop(0))
            self._build_minheap(list, n-i)  
        
        return list
