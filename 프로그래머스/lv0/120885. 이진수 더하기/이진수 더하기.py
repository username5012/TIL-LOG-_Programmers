def solution(bin1, bin2):
    answer = ''
    bin1 = int(bin1, 2)
    bin2 = int(bin2, 2)
    
    answer = bin(bin1 + bin2)
    answer = answer[2:]
    return answer