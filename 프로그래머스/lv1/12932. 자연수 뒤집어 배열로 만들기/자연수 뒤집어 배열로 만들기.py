def solution(n):
    answer = []
    end = len(str(n))-1
    for i in range (end, -1, -1):
        answer += [int(str(n)[i])]
    return answer