def solution(numLog):
    answer = ''
    
    for i in range(1, len(numLog)):
        A = numLog[i] - numLog[i-1]
        if A == 1:
            answer += 'w'
        elif A == -1:
            answer += 's'
        elif A == 10:
            answer += 'd'
        elif A == -10:
            answer += 'a'
        

        
    return answer