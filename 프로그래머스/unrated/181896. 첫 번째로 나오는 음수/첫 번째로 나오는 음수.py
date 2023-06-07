def solution(num_list):
    answer = 0
    minus = 0
    
    for i in num_list:
        if i < 0:
            minus = i
            break
            
    if minus != 0:
        answer = num_list.index(minus)
    else:
        answer = -1
    
    return answer