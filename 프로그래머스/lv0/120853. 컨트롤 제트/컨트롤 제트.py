def solution(s):
    answer = 0
    S = s.split(' ')
    print(S)
    
    for i in range(len(S)):
        if S[i] != 'Z':
            answer += int(S[i])
            
        else:
            answer -= int(S[i-1])
        
    
    return answer