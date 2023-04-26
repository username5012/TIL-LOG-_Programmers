def solution(chicken):
    answer = 0
    coup = chicken
    
    while coup >= 10:
        eaten = coup // 10 
        answer += eaten 
        coup = coup % 10 + eaten 
    

    return answer