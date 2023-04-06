def solution(emergency):
    answer = []
    order = sorted(emergency, reverse=True)
    print(order)
    for i in range(len(order)):
        a = order.index(emergency[i]) +1
        answer.append(a)
        

    return answer