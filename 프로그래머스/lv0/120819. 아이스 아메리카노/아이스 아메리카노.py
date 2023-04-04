def solution(money):
    answer = []
    EA = money // 5500
    charge = money % 5500
    answer.append(EA)
    answer.append(charge)
    return answer