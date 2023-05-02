def solution(n):
    answer = ''
    another_n = list(str(n))
    another_n = sorted(another_n, reverse=True)
    
    for i in range (len(another_n)):
        answer += another_n[i]
        
    answer = int(answer)
    return answer