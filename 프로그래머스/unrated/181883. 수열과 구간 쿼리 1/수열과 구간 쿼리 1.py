def solution(arr, queries):
    answer = []
    for query in queries:
        s, e = query[0], query[1]
        for i in range (s, e+1):
            arr[i] += 1
            
    return arr