def solution(array, height):
    answer = 0
    for cm in array:
        if cm > height :
            answer += 1
    return answer