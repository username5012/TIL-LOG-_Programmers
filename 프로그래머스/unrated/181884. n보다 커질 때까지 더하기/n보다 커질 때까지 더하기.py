def solution(numbers, n):
    answer = 0
    plus = 0
    
    for i in range(len(numbers)):
        plus += numbers[i]
        if plus > n:
            answer = plus
            break
            
    return answer