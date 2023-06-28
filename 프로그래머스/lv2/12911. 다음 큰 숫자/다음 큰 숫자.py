def binary_one(n):
    cnt = str(bin(n)[2:]).count('1')
    
    return cnt

def solution(n):
    answer = 0
    cnt_n = binary_one(n)
    
    while True:
        n += 1
        cnt_other = binary_one(n)
        
        if cnt_n == cnt_other:
            answer = n
            break
        
    return answer