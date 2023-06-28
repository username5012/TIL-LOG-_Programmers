
def solution(n):
    
    fib_list = []
    
    for i in range (n+1):
        
        if i == 0:
            fib_list += [0 % 1234567] 
            
        elif i == 1 or i == 2:
            fib_list += [1 % 1234567]
            
        else:
            sum_fib = fib_list[i-1] + fib_list[i-2]
            fib_list += [sum_fib % 1234567]
    
    
    answer = fib_list[n]
    
    
    return answer