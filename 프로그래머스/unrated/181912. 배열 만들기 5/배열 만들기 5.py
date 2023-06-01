def solution(intStrs, k, s, l):
    answer = []
    
    for idx in intStrs:
        cut = int(idx[s:s+l])
        if cut > k:
            answer += [cut]

            
    return answer