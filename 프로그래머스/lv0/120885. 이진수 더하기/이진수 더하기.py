def solution(bin1, bin2):
    answer = ''
    # 2진수를 10진수로 바꿔주기
    bin1 = int(bin1, 2)
    bin2 = int(bin2, 2)
    
    # 10진수로 바꾼 두 수를 더하고 2진수로 바꾸기
    answer = bin(bin1 + bin2)
    
    # 파이썬 2진수 변환 시 생기는 앞의 '0b' 제거
    answer = answer[2:]
    return answer