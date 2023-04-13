def solution(n):
    answer = []
    for i in range (2, n+1):
        while True:                 # i 값으로 나눠준 뒤 다시 처음부터 i 사이클 돌리기 (ex. 2, 2, 3, 3, 5 ...)
            if n % i == 0:
                answer.append(i)
                n = n//i
            else:
                break
                
    answer = list(set(answer))      # 중복값 제거
    answer = sorted(answer)         # 오름차순

                
    return answer