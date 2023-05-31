def sum_V (a, b):
    result = True  
    if a == False and b == False:
        result = False
    
    return result

def sum_A (a, b):
    result = False  
    if a == True and b == True:
        result = True
    
    return result
    
        
    


def solution(x1, x2, x3, x4):
    answer = True
    
    X1 = sum_V(x1, x2)
    X2 = sum_V(x3, x4)
    
    answer = sum_A(X1,X2)
    
    return answer