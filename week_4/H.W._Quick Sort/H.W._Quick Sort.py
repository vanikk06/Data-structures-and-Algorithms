def quick_sort(list):
    if len(list) <= 1:                    #先判斷list是否是可以比大小的
        return list
    
    bigger = []                          #創造一個空間放大於key的值，最後在一起往後加
    
    key = list[-1]                       #將最後一個值設為key
    i = 0
    while i < len(list):                 #一個個與key比較
        if list[i] <= key:               #<=key就放著不動，往下一個繼續比
            i += 1
        else:                            #>key就抓出來放到剛剛建立的空間，並把它在原本的list上刪除
            bigger.append(list.pop(i))      #因為原本的值被刪除，index改變，所以i不加1
    
    key_list = []                        #把檢查過後的key抓出來另外放，並從原本的list上刪除
    key_list.append(list[-1])            
    list.pop()
    
    list = quick_sort(list)              #遞迴式執行
    bigger = quick_sort(bigger)
    return list+key_list+bigger
