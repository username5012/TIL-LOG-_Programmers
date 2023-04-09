def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        plus = []
        for j in range(n):
            plus.append(num_list[i+j])
        
        answer += [plus]
    
    return answer