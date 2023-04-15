def solution(dots):
    answer = 0
    width_dot = []
    height_dot = []
    
    for i in range(len(dots)):
        width_dot += [dots[i][0]]
        
    for j in range(len(dots)):
        height_dot += [dots[j][1]]
        
        
    print(width_dot)
    print(height_dot)
    width = max(width_dot) - min(width_dot)
    height = max(height_dot) - min(height_dot)
    
    answer = width * height
    
    return answer