def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if stk == []:
            stk += [arr[i]]
            i += 1
            
        else:
            if stk[-1] < arr[i]:
                stk += [arr[i]]
                i += 1
                
            else:
                stk.pop(-1)
                
    return stk