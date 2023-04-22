def solution(babbling):
    can_speak = ['aya', 'ye', 'woo','ma']
    answer = 0
    for i in range(len(babbling)):
        change = babbling[i]
        for speak in can_speak:
            if speak in babbling[i]:
                change = change.replace(speak,' ')
                print(change)
        change = change.replace(' ','')
        if change == "":
            answer += 1
    return answer