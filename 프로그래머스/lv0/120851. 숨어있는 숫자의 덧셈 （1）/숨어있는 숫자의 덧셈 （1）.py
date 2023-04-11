def solution(my_string):
    answer = 0
    num_list = []
    for i in range (1, 10):
        num_list += [str(i)]
    
    for j in my_string:
        if j in num_list:
            answer += int(j)
    return answer