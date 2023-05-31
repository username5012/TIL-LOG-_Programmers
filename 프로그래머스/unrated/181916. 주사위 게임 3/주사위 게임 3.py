def solution(a, b, c, d):
    answer = 0
    dice = [a,b,c,d]
    set_dice = list(set(dice))
    
    if len(set_dice) == 1:
        answer = 1111 * a
        
        
    elif len(set_dice) == 2:
        
        if dice.count(set_dice[0]) == 2:
            p = set_dice[0]
            q = set_dice[1]
            
            answer = (p+q) * abs(p-q)
            
            
        else:
            if dice.count(set_dice[0]) == 1:
                p = set_dice[1]
                q = set_dice[0]
                
                
            else:
                p = set_dice[0]
                q = set_dice[1]    
                
            answer = (10 * p + q) ** 2
        
        
        
    elif len(set_dice) == 3:
        p,q,r = 0, 0, 0
        
        for i in set_dice:
            if dice.count(i) == 2:
                p = i
                
            else:
                if q == 0:
                    q = i
                else:
                    r = i
        
        answer = q * r 
        
    elif len(set_dice) == 4:
        answer = min(dice)


            
    return answer