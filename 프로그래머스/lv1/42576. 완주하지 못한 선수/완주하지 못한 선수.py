from collections import Counter

def solution(participant, completion):
    answer = ''
    
    p_dict = Counter(participant)
    c_dict = Counter(completion)
    
    
    no_goal = p_dict - c_dict
    
    answer = list(no_goal)[0]
    
                       
    return answer