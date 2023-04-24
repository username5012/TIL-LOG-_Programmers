def solution(A, B):
    answer = -1
    
    for i in range(len(A)):
        C = ''
        C += A[-i:]
        C += A[:-i]
        
        if C == B:
            answer = i
            break
        
    return answer