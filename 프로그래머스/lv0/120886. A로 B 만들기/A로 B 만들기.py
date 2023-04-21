def solution(before, after):
    answer = 0
    
    
    spl_bef = []
    spl_aft = []
    
    for i in range (len(before)):
        spl_bef += [before[i]]
    for j in range (len(after)):
        spl_aft += [after[j]]
        
    spl_bef = sorted(spl_bef)
    spl_aft = sorted(spl_aft)
    
    if spl_bef == spl_aft:
        answer = 1
        
        
    
        
                    
    return answer