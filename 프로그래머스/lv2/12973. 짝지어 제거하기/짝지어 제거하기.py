def solution(s):
    answer = -1
    
    # stack 개념 사용
    stack = []
    
    for i in range (len(s)):
        # 리스트에 아무것도 없을 경우, 추가
        if not stack:
            stack.append(s[i])
            
        else:
            # 리스트에 있을 경우,
            # 1) 알파벳이 짝일 경우, 둘다 제거 (stack의 1개를 빼고, s[i]를 더하지 않음으로, 둘다 제거하는 개념)
            if s[i] == stack[-1]:
                stack.pop()
                
            else:
            # 2) 알파벳이 짝이 아닐 경우, 둘다 살림.
                stack.append(s[i])
    
    print(stack)
    
    if stack:
        answer = 0
    
    else:
        answer = 1

    return answer