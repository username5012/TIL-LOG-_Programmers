def solution(num_list):
    answer = 0
    plus = 0
    multiple = 1
    
    for i in range(len(num_list)):
        plus += num_list[i]
        multiple *= num_list[i]
        
        
    plus = plus ** 2
    print(plus, multiple)
    if plus > multiple:
        answer = 1
    return answer