def solution(numbers, k):
    people = 1
    cnt = 1
    while True:
        cnt += 1
        print(cnt)
        
        if people + 2 > numbers[-1]:
            people = people - numbers[-1] + 2
            
        else:
            people = people + 2
        
        if cnt == k:
            break
                
    return people