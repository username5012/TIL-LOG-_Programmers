def solution(arr):
    answer = arr.copy()
    answer.remove(min(answer))
    
    if answer == []:
        answer += [-1]
    
    return answer