def solution(s):
    answer = True
    
    s = s.lower()
    
    cnt_p = 0
    cnt_y = 0
    
    for i in range(len(s)):
        if s[i] == 'p':
            cnt_p += 1
        elif s[i] == 'y':
            cnt_y += 1
            
            
    if cnt_p == cnt_y:
        answer = True
        
    else:
        answer = False
    

    return answer