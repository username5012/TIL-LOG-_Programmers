def solution(d, budget):
    answer = 0
    d.sort()
    for num in d:
        if num <= budget:
            answer += 1
            budget -= num
        else:
            break
            
    return answer