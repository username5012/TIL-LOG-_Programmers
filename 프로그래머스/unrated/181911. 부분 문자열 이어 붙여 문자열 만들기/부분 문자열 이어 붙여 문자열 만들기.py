def solution(my_strings, parts):
    answer = ''
    
    for i in range (len(parts)):
        s, e = parts[i][0], parts[i][1]
        print(s,e)
        
        answer += my_strings[i][s:e+1]
        
    return answer