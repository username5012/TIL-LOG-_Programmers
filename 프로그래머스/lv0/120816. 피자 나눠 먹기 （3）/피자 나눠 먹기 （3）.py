def solution(slice, n):
    answer = 0
    i = 0 
    while True:
        i += 1
        if slice * i >= n:
            break
    answer = i
    return answer