#建立heap的樹狀結構：Maxheap
    # To heapify subtree rooted at index i.
    # n:size of heap
    

def heapify(arr, n, i):
    largest = i    #最初的largest
    left = 2*i+1   #左邊孩子
    right = 2*i+2  #右邊孩子
    
    if left < n and arr[i] < arr[left]:          #與左邊孩子比較
        largest = left
        
    if right < n and arr[largest] < arr[right]:  #與右邊孩子比較
        largest = right
        
    if largest != i:                             #交換
        arr[i], arr[largest] = arr[largest], arr[i]
        
        heapify(arr, n, largest)                 #繼續往下比
        
        
#用剛剛建起的樹狀結構來進行排序
    # The main function to sort an array of given size

def heap_sort(arr):
    n = len(arr)
    
    # Build a maxheap.
    for i in range(n):
        heapify(arr, n, i)
        
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] #交換
        heapify(arr, i, 0)              #改變size of heap
