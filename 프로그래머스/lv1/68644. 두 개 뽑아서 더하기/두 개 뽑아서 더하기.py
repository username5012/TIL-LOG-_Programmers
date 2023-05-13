from itertools import combinations

def solution(numbers):
    answer = []
    
    for i,j in combinations(numbers, 2):
        if i+j not in answer:
            answer += [i+j]
            
    answer = sorted(answer)   
    
    return answer