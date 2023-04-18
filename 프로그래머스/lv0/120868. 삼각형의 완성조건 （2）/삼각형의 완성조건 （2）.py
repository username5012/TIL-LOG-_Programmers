
def solution(sides):
    answer = 0
    a, b = min(sides), max(sides)
    
    for i in range(1, sum(sides)):
        # 길이, 정수이기 때문에 1부터 시작해서 최대는 sides의 합 | Why? i가 가장 큰 경우는 i가 가장 긴 변일 경우. 이 때, i는 sum(sides)보다 작아야 함.
        
        if i >= b:  # i가 가장 긴 변인 경우
            if i < a + b: # 가장 긴 변 < 다른 두 변의 길이의 합
                print (a, b, i)
                answer += 1
                
        elif i < b: # side 내의 변이 가장 긴 변인 경우,
            if b < a + i: # 가장 긴 변 < 다른 두 변의 길이의 합
                print (a, b, i)
                answer += 1

                
    return answer


