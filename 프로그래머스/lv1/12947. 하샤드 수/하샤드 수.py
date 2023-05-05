def solution(x):
    answer = True
    hashad = 0
    for i in str(x):
        hashad += int(i)
        
    if x % hashad == 0:
        answer = True
    else:
        answer = False
    
    return answer