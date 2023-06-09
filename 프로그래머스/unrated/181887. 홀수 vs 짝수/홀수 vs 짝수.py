def solution(num_list):
    answer = 0
    A = sum(num_list[::2])
    B = sum(num_list[1::2])

    if A >= B :
        answer = A
    else:
        answer = B
    return answer