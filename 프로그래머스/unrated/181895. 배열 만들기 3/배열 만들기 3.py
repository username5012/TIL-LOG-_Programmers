def solution(arr, intervals):
    answer = []
    
    for interval in intervals:
        a, b = interval[0], interval[1]
        answer += arr[a:b+1]
        
    return answer