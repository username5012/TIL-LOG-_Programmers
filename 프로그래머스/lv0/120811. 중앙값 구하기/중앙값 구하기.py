def solution(array):
    answer = 0
    array = sorted(array)
    i = len(array) // 2
    answer = array[i]
    return answer