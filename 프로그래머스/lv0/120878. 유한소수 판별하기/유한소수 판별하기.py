from math import gcd

def solution(a, b):
    answer = 2
    
    # 최대공약수로 기약분수 만들기
    max_div = gcd(a,b)
    a = a // max_div
    b = b // max_div
    print(a, b)
    
    # 분자 == 분모일 경우, 분모와 상관없이 유한소수
    if a == b:
        answer = 1
    
    # 분자 != 분모일 경우, 분모의 소인수가 2,5만 있어야함.
    else:
        b_div = []
        
        # for, while문 사용해서 분모의 소인수 구하기.
        for i in range (2, b+1):
            while b % i == 0:
                b_div += [i]
                b = b // i
        
        print(b_div)
        
        # b_div 내의 숫자가 2, 5 이외에 다른 수가 없을 경우, 유한소수.
        if all (x in (2, 5) for x in b_div):
            answer = 1
            

    return answer