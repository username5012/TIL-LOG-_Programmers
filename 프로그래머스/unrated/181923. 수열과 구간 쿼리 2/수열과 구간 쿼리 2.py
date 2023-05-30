def solution(arr, queries):
    answer = []
    
    for query in queries:
        i,j,k = query[0], query[1], query[2]
        mini = []
        for i in arr[i:j+1]:
            if i > k:
                mini += [i]
        
        if mini == []:
            answer += [-1]
        else:
            answer += [min(mini)]
        
        
        
        
        
    
    return answer