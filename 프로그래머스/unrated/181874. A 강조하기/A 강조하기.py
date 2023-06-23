def solution(myString):
    answer = ''
    
    for i in myString:
        if i == 'A' or i == 'a':
            answer += i.upper()
        else:
            answer += i.lower()
            
    return answer