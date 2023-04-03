def solution(n):
    answer = 0
    A = 0
    B = 0
    C = 0
    if n % 6 == 0:
        answer = n // 6
    else:
        for i in range (1, (6*n+1)):
            if i % 6 == 0 and i % n == 0:
                answer = i // 6
                break
    
    return answer