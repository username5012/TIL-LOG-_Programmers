def solution(a, b):
    answer = 0
    A = int(str(a)+str(b))
    B = int(str(b)+str(a))
    
    if A >= B:
        answer = A
    else:
        answer = B
    
    
    return answer