def solution(arr):
    answer = []
    
    if arr.count(2) == 0:
        answer = [-1]
        
    elif arr.count(2) == 1:
        answer = [2]
        
    else:
        a = arr.index(2)
        b = len(arr) - arr[::-1].index(2)
        
        answer = arr[a:b]
        
    
    
    
    return answer