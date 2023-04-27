def solution(arr, divisor):
    answer = []
    
    for num in arr:
        if num % divisor == 0:
            answer += [num]
            
    answer = sorted(answer)
   
    if answer == []:
        answer = [-1]
    return answer