def solution(myString, pat):
    answer = ''
    
    for i in range(len(myString)):
        if myString[i:i+len(pat)] == pat:
            answer = myString[:i+len(pat)]            
                               
    return answer