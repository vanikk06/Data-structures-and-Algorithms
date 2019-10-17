def quick_sort(list):
    key_list = []
    small_list = []
    big_list = []
    
    if len(list) <= 1:                    #排除list空的、只有一個值的情況
        return list                    #若無list，會出現(TypeError: unsupported operand type(s) for +: 'NoneType' and 'list')
    
    key = list[0]                         #將index[0]設為key
    for i in list:
        if i > key:                       #大於key的值放入big_list
            big_list.append(i)
        elif i < key:                     #小於key的值放入small_list
            small_list.append(i)          
        else:                             #等於key的值放入key_list
            key_list.append(i)
            
    #再對未排序的small_list與big_list重複相同的動作
    small_list = quick_sort(small_list)  
    big_list = quick_sort(big_list)
    return small_list+key_list+big_list
