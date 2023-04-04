def solution(num_list):
    answer = []
    num = len(num_list)
    print(num)
    
    for i in range(num-1,-1,-1):
        answer.append(num_list[i])

    return answer