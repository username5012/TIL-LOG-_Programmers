from collections import Counter

def solution(participant, completion):
    answer = ''
    
    # 참가자와 완주자를 카운터를 이용하여 딕셔너리로 만듬 | 동명이인까지 확인 가능
    p_dict = Counter(participant)
    c_dict = Counter(completion)
    
    # 참가자 명단에서 완주자 명단을 뺌. 
    no_goal = p_dict - c_dict
    
    # Counter 형태에서 리스트로 만들면 키값만 리스트로 들어감. | 리스트의 1번째 (리스트 내에는 1개의 이름밖에 없음) 가 정답.
    answer = list(no_goal)[0]
    
                       
    return answer