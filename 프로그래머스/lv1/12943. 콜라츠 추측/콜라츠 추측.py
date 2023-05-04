def solution(num):
    answer = 0
    while True:
        if num == 1:
            break
            
        else:
            if num % 2 == 0:
                num = num // 2
                answer += 1
                print(num)

            else:
                num = num * 3 + 1
                answer += 1
                print(num)

    if answer > 500:
        answer = -1
    return answer