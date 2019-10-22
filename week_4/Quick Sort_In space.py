def quick_sort_temp(list, left, right):
    if left >= right:
        return list
        
    
    key = list[left]
    left_point = left
    right_point = right
    
    while left_point < right_point:    #在left_point < right_point情況下進行，不用擔心相遇
        while left_point < right_point and key <= list[right_point]:  #從右向左，當有小於key時跳出
            right_point -= 1
        while left_point < right_point and key >= list[left_point]:   #從左向右，當有大於key時跳出
            left_point += 1
        if left_point < right_point:                                  #交換
            list[left_point], list[right_point] = list[right_point], list[left_point]
            
    list[left], list[right_point] = list[right_point], list[left]   #left_point與right_point相遇時,必定在left_point = right_point的情況下
    #list[left], list[left_point] = list[left_point], list[left]    #因為是right_point先確定，left_point再移動
    
    
    #遞迴式的重複執行
    quick_sort_temp(list, left, left_point-1)
    quick_sort_temp(list, right_point+1, right)
    return list

def quick_sort(list):
    return quick_sort_temp(list, 0, len(list)-1)
