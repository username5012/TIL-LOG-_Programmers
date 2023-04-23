def solution(i, j, k):
    answer = 0
    
    for a in range (i, j+1):
        k = str(k)
        a = str(a)
        if k in a:
            answer += a.count(k)
            print(answer)
    return answer