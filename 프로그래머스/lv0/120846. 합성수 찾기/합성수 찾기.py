def prime (x):
    flag = True
    
    if x < 2:
        flag = False
    
    for i in range (2, x):
        if x % i == 0:
            flag = False
    
    return flag

def solution(n):
    answer = 0
    
    for a in range (2, n+1):
        if prime(a) == False:
            answer += 1

    return answer