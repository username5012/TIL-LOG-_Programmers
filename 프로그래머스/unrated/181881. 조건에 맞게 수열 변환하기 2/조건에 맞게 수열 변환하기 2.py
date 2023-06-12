def solution(arr):
    answer = 0
    next = []
    
    while True:
        answer += 1
        
        for i in range (len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                next += [arr[i] // 2]
            elif arr[i] < 50 and arr[i] % 2 == 1:
                next += [(arr[i] * 2) + 1]
            else:
                next += [arr[i]]
        
        if next == arr:
            break
        
        else: 
            arr = next
            next = []
            
    return answer-1