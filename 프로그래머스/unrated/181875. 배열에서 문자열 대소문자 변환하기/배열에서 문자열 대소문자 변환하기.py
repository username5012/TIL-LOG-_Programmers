def solution(strArr):
    answer = []
    
    for i in range(len(strArr)):
        if i % 2 != 0 :
            answer += [strArr[i].upper()]
        else:
            answer += [strArr[i].lower()]
            
    return answer