from string import ascii_uppercase, ascii_lowercase

def solution(s, n):
    upper = list(ascii_uppercase)*2
    lower = list(ascii_lowercase)*2
    
    print(upper)

    
    answer = ''
    
    for alp in s:
        
        if alp in upper:
            idx = upper.index(alp)
            final = upper.index('Z')
            
            if idx + n > final:
                answer += upper[idx+n-final-1]
                
            else:
                answer += upper[idx+n]
        
        
        elif alp in lower:
            idx = lower.index(alp)
            final = lower.index('z')
            
            if idx+n > final:
                answer += lower[idx+n-final-1]
                
            else:
                answer += lower[idx+n]
            
            
        else:
            answer += alp
            

        
    return answer