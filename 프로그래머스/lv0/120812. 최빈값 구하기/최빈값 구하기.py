

def solution(array):
    answer = 0
    keys = list(set(array))
    # 숫자가 1개밖에 없을 경우
    print(keys)
    if len(keys) == 1:
        answer = keys[-1]
    
    # 숫자가 2개 이상일 경우,
    else:
        # array 내의 중복값 제거한 정수 리스트를 만든다.

        
        # array 내에서 keys가 반복되는 횟수 리스트를 만든다.
        values = []
        for i in keys:
            values.append(array.count(i))
        print(values)
        
        # 오름차순으로 해서 최댓값 구하기
        sort_values = sorted(values)
        max_cnt = sort_values[-1]
        
        # 오름차순한 리스트에서 마지막 값 제외한 나머지가 최댓값과 중복되는 지 확인
        for j in range(len(values)-1):
            # 중복될 경우, -1
            if max_cnt == sort_values[j]:
                answer = -1
            # 중복되지 않을 경우, 최댓값과 상응하는 keys 값 꺼내기
            else:
                idx = values.index(max_cnt) # 오름차순하지 않은 리스트의 최댓값 인덱스번호 구하기
                answer = keys[idx] # values값과 같은 위치의 키값을 꺼내주기
    
    
    return answer