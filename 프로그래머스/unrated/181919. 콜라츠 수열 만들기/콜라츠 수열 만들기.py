def solution(n):
    answer = []
    while True:
        
        if n == 1:
            answer += [n]
            break
            
        else:
            if n % 2 == 0:
                answer += [n]
                n = n // 2
            else:
                answer += [n]
                n = (n * 3) + 1
            
        
            
    return answer