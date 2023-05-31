def solution(l, r):
    answer = []
    for i in range(l, r+1):
        I = str(i)
        cnt = 0
        
        for j in I:
            if j == '5' or j == '0':
                cnt += 1
        
        if cnt == len(str(i)):
            answer += [i]
            
    
    if answer == []:
        answer = [-1]
    
    return answer