# 길이 구하는 공식
def length(dots):
    if len(dots) >= 2:
        length = len(dots) -1
    else:
        length = 0

    return length
        

def solution(lines):
    answer = 0
    
    A = []
    B = []
    C = []
    
    # 각 lines에 포함되는 dots 원소 정리 (겹치는 부분을 알아내기 위해)
    
    for i in range (lines[0][0], lines[0][1]+1):
        A += [i]
    for j in range (lines[1][0], lines[1][1]+1):
        B += [j]
    for k in range (lines[2][0], lines[2][1]+1):
        C += [k]
        
    print(A, B, C)
    
    
    # 겹치는 부분 확인
    
    AB = set(A)&set(B)
    BC = set(B)&set(C)
    CA = set(C)&set(A)
    
    print(AB, BC, CA)
    print(AB&BC, BC&CA, CA&AB)

    
    # 겹치는 선분인 AB, BC, CA의 길이를 더한 다음 | AB, BC, CA끼리 겹치는 부분의 길이를 빼고, | AB, BC, CA 모두 겹치는 부분의 길이를 더해줌.
    
    answer = length(AB) + length(BC) + length(CA) - length(AB&BC) - length(BC&CA) - length(CA&AB) + length(AB&BC&CA)
    
    
    
    
    
    
    
    return answer



#     A = []
#     B = []
#     C = []
    
#     for i in range (lines[0][0], lines[0][1]+1):
#         A += [i]
#     for j in range (lines[1][0], lines[1][1]+1):
#         B += [j]
#     for k in range (lines[2][0], lines[2][1]+1):
#         C += [k]
        
        
    
#     AB = set(A)&set(B)
#     BC = set(B)&set(C)
#     AC = set(A)&set(C)
    
#     if len(AB) == 1:
#         AB = set('')
        
#     if len(BC) == 1:
#         BC = set('')
        
#     if len(AC) == 1:
#         AC = set('')
    

#     print(AB, BC, AC)
    
#     answer = list(AB|BC|AC)
    
#     if len(answer) >= 2:
#         answer = len(answer) - 1
        
#     elif len(answer) < 2:
#         answer = len(answer)