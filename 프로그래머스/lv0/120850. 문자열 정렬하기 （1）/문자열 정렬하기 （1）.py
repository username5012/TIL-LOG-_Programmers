def solution(my_string):
    answer = []
    num_list = []
    for i in range (0, 10):
        num_list += [str(i)]
        
    for j in my_string:
        print(j)
        if j in num_list:
            print(j)
            answer += [int(j)]
            
    answer = sorted(answer)
    return answer