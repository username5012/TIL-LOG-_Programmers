def solution(s):
    answer = []
    s = s.split(' ')
    
    for word in s:
        print(s)
        change = ''
        for i in range (len(word)):
            if i % 2 == 0:
                change += word[i].upper()
                
            else:
                change += word[i].lower()
                
        answer += [change]
        
    answer = ' '.join(answer)
                
    
    return answer