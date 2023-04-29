from string import ascii_uppercase, ascii_lowercase


def solution(s):
    answer = True
    
    upper = list(ascii_uppercase)
    lower = list(ascii_lowercase)
    
    if len(s) != 4 and len(s) != 6:
        answer = False
        
    for i in range (len(s)):
        if s[i] in upper or s[i] in lower:
            answer = False
    
    
    
    return answer