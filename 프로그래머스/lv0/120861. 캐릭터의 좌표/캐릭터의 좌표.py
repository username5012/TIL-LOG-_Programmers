def solution(keyinput, board):
    answer = []
    
    min_X = -(board[0] // 2)
    max_X = (board[0] // 2)
    min_Y = -(board[1] // 2)
    max_Y = (board[1] // 2)
    
    print(min_X)
    print(max_X)
    print(min_Y)
    print(max_Y)
    
    start = [0,0]
    
    
    
    
    for i in keyinput:
        if i == "left":
            if min_X < start[0]:
                start[0] -= 1
                print(start)
                
            else:
                print(start)
                pass
            
            
        if i == "right":
            if start[0] < max_X:
                start[0] += 1
                print(start)
                
            else:
                print(start)
                pass
            
        if i == "up":
            if start[1] < max_Y:
                start[1] += 1
                print(start)
                
            else:
                print(start)
                pass            
            
        if i == "down":
            if min_Y < start[1]:
                start[1] -= 1
                print(start)
                
            else:
                print(start)
                pass    
            

    return start