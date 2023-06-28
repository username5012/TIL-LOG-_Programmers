def solution(n):
    answer = []
    
    for i in range (1, n+1):
        if i == 1:
            answer += [1 % 1234567]
            
        elif i == 2:
            answer += [2 % 1234567]
            
        else:
            answer += [(answer[i-2] + answer[i-3]) % 1234567]
            
    

    
    return answer[-1]