def solution(a, b):
    answer = ''
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [4, 6, 9, 11]
    month_29 = [2]
    
    day = 0
    
    for i in range (1, a):
        print(i)
        
        if i in month_31:
            day += 31
        elif i in month_30:
            day += 30
        else:
            day += 29
            
    day += b
    day = day % 7

    answer = week[day-1]
    
    
    return answer