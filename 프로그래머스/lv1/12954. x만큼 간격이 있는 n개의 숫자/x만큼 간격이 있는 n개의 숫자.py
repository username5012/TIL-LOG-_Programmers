def solution(x, n):
    answer = []
    end = x * n
    
    if x > 0:
        for num in range (x, end+1, x):
            answer += [num]
            
            if len(answer) == n:
                break
        
    elif x < 0:
        for num in range(x, end-1, x):
            answer += [num]
            
            if len(answer) == n:
                break
                
    else:           
        for num in range (n):
            answer += [0]
            
            
    return answer