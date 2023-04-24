def solution(A, B):
    answer = -1
    
# C => A를 i만큼 이동했을때 나오는 단어
    for i in range(len(A)):
        C = ''
        C += A[-i:]
        C += A[:-i]
        
# A를 i만큼 움직인 C가 B와 같을 경우, answer는 i.
        if C == B:
            answer = i
            break
        
    return answer