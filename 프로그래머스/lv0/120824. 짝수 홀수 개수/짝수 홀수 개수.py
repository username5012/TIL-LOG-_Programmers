def solution(num_list):
    answer = []
    Hol = 0
    Jjak = 0
    for num in num_list:
        if num % 2 != 0:
            Hol += 1
        else :
            Jjak += 1
    
    answer.append(Jjak)
    answer.append(Hol)
    
    return answer