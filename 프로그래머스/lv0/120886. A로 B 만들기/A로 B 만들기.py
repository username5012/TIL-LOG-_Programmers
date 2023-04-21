def solution(before, after):
    answer = 0
    
    # 해당 문제는 순서를 배제한 두 단어의 알파벳이 같을 경우 1, 아닐 경우 0이 나오는 문제
    
    
    # 1. 두 단어를 스플릿해서 리스트에 넣어 알파벳의 종류, 개수를 파악
    spl_bef = []
    spl_aft = []
    
    for i in range (len(before)):
        spl_bef += [before[i]]
    for j in range (len(after)):
        spl_aft += [after[j]]

    # 2. 리스트를 오름차순해서, 두 단어 리스트의 순서 규칙을 동일하게 만들어줌 => 해당 조건으로 알파벳 종류와 갯수만 파악할 수 있게 조건 부여.
    
    spl_bef = sorted(spl_bef)
    spl_aft = sorted(spl_aft)
    
    
    # 3. 위에서 맞춘 두 단어의 리스트가 동일할 경우, 1 도출
    if spl_bef == spl_aft:
        answer = 1
        
        
    
        
                    
    return answer