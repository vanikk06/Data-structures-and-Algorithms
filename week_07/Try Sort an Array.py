class Solution:  
            
    def _divide(self, list, n:int):
        if n <= 1:                           
            return list
                                             
        left = []                              
        right = []                      
    
        n1 = int(n/2)
        n2 = n - n1                     
                                 
        for i in range(n1):                  
            left.append(list[i])
    
        for j in range(n1, n):               
            right.append(list[j])
           
        left = self._divide(left, n1)        
        right = self._divide(right, n2)
    
        return self._merge(left, right)      
    
    
    def _merge(self, left, right):    
        temp = []                           
    
        n1, n2 = len(left), len(right)               
    
        i = 0
        j = 0
        while i < n1 and j < n2:            
            if left[i] < right[j]:
                temp.append(left[i])
                i += 1
            else:
                temp.append(right[j])
                j += 1
    
        if i == n1:                         
            while j < n2:
                temp.append(right[j])
                j += 1
        else:
            while i < n1:                   
                temp.append(left[i])
                i += 1
    
        return temp                         
 
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return self._divide(nums, n)
