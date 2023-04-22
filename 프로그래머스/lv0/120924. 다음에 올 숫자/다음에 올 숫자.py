def solution(common):
    answer = 0 # 마지막에 나올 수
    num = 0 # 등차 or 등비
    cnt = []

    # common 안의 수의 관계 구하기 | 인접한 두 숫자의 차를 리스트에 넣기
    for i in range (len(common)-1):
        cnt += [common[i+1] - common[i]]
    
    
    print(cnt)
    
    # 인접한 두 숫자의 차 리스트 내의 숫자가 같을 경우에는 등차수열.
    
    if cnt[0] == cnt[1]:
        num = cnt[0]
        answer = common[-1] + num
    
            
    # 인접한 두 숫자의 차 리스트 내의 숫자가 다를 경우에는 등비수열.       
    else:
        num = cnt[1] // cnt[0]
        answer = common[-1] * num
        
                   
            
    return answer