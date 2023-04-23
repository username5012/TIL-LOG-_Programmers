def solution(num, total):
    answer = []
    
    # 짝수
    if num % 2 == 0:
        
        div = num // 2
        num_std = total // div
        print(num_std)
        
        a = num_std // 2
        b = (num_std//2) + 1
        
        
        answer += [a,b]
        
        while True:
            a -= 1
            b += 1
            answer += [a, b]
            
            if len(answer) == num:
                break
            
        answer = sorted(answer)
        
    # 홀수
    else:
        num_std = total // num
        answer += [num_std]
        print(num_std)
        
        div = num // 2
        print(div)
        
        for i in range (1, div+1):
            num_plus = num_std + i
            num_minus = num_std - i
            
            answer += [num_plus, num_minus]
            
        
        answer = sorted(answer)
            
        
    return answer



