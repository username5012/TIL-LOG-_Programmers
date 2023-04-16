def solution(polynomial):
    answer = ''
    numbers = polynomial.split(" + ")
    list_x = []
    list_num = []
    for num in numbers:
        if 'x' in num:
            list_x.append(num)
        else:
            list_num.append(num)
    
    # 일차항 구하기
    x_num = []
    for i in list_x:
        if i == "x":
            x_num += [1]
        elif i == "-x":
            x_num += [-1]
        else:
            x_num += [i[:-1]]
            
    x_num = map(int, x_num)
    x_num = sum(x_num)
    
    
    # 상수항 구하기
    list_num = map(int, list_num)
    sum_num = sum(list_num)
    
    
    
    # 수식 만들기
    
    if x_num == 1:
        if sum_num == 0:
            answer = 'x'     
            
        else:
            answer = 'x + ' + str(sum_num)  
        
    elif x_num == -1:
        if sum_num == 0:
            answer = '-x' 
            
        else:
             answer = '-x + ' + str(sum_num) 
        
    elif x_num == 0:
        if sum_num == 0:
            answer = '0'
            
        else:
            answer = str(sum_num)
    
        
    else:
        if sum_num == 0:
            answer = str(x_num) +'x'
            
        else:
            answer = str(x_num) +'x + ' + str(sum_num)
        
    
    
    
    
    
    print(answer)
    
    
            
    
    return answer