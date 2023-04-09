def facto(n):
    factorial = 1
    for i in range (1, n+1):
        factorial *= i
    
    return factorial


def solution(balls, share):
    n = facto(balls)
    r = facto(share)
    g = facto(balls-share)
    
    answer = n / (r * g)
        
    return answer

# 조합(nCr)
# = n! / r! (n-r)!
    
