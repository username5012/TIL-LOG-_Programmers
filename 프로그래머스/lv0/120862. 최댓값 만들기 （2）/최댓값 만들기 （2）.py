def solution(numbers):
    answer = 0
    numbers=sorted(numbers)
    a = numbers[0] * numbers[1]
    b = numbers[-1] * numbers[-2]
    
    if a >= b :
        answer = a
        
    else:
        answer = b
    
    return answer