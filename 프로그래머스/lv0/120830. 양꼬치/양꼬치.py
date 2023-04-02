def solution(n, k):
    answer = 0
    a = n * 12000
    b = k * 2000
    c = (n // 10) * 2000
    
    answer = a + b - c
    
    
    return answer