def solution(n):
    answer = 0
    N = 1
    mul = 1
    
    if n == 1:
        answer = 1
        
    else:
        while N < n:
            answer += 1
            N = N * mul

            if N < n:
                mul += 1

            elif N == n:
                print('=')
                break

            elif N > n:
                answer -= 1
                print('-')
                break


            
    return answer