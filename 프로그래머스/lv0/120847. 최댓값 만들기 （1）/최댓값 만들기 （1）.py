def solution(numbers):
    answer = 0
    numbers_1 = sorted(numbers)
    answer = numbers_1[-1] * numbers_1[-2]
    return answer