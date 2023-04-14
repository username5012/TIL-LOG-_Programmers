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
    
    
    for i in range (lines[0][0], lines[0][1]+1):
        A += [i]
    for j in range (lines[1][0], lines[1][1]+1):
        B += [j]
    for k in range (lines[2][0], lines[2][1]+1):
        C += [k]
        
    print(A, B, C)
    
    AB = set(A)&set(B)
    BC = set(B)&set(C)
    CA = set(C)&set(A)
    
    print(AB, BC, CA)
    print(AB&BC, BC&CA, CA&AB)

    
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