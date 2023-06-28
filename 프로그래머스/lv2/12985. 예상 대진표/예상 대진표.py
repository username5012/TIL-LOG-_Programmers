def solution(N,A,B):
    answer = 0
    
    while True:
        answer += 1
        
        
        if A % 2 == 1:
            A = (A // 2) + 1
        else:
            A = A // 2
            
        if B % 2 == 1:
            B = B // 2 + 1
        else:
            B = B // 2
        
        print(A, B)
        
        if A == B:
            break

            
    return answer