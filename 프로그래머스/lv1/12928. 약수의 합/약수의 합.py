def solution(n):
    answer = 0
    div_list = []
    
    for i in range (1, n+1):
        if n % i == 0:
            div_list += [i]
            
    answer = sum(div_list)
    
    return answer