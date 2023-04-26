from math import gcd

def solution(a, b):
    answer = 2
    
    max_div = gcd(a,b)
    a = a // max_div
    b = b // max_div
    print(a, b)
    
    if a == b:
        answer = 1
        
    else:
        b_div = []
        
        for i in range (2, b+1):
            while b % i == 0:
                b_div += [i]
                b = b // i
        
        print(b_div)
        
        if all (x in (2, 5) for x in b_div):
            answer = 1
            

    return answer