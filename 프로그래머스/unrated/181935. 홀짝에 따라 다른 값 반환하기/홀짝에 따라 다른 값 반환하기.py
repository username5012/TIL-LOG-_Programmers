def solution(n):
    answer = 0
    
    for i in range(n+1):
        if n % 2 != 0:
            if i % 2 != 0:
                answer += i
        else:
            print(i)
            if i % 2 == 0:
                answer += i ** 2
        
    return answer