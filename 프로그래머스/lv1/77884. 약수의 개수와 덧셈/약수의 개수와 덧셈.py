def counting(num):   # 입력된 수의 약수의 개수를 계산해주는 함수 
    number = 0
    for i in range(1,num+1):
        if num% i == 0:
            number+=1 
    
    return number 
    
def solution(left, right):  
    answer = 0
    for i in range(left, right+1):
        if counting(i)%2 == 0:    # 약수의 개수가 짝수이면 +, 홀수이면 -
            answer+= i
        else :
            answer-= i 
        
    return answer