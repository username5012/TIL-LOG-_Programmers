from string import ascii_uppercase, ascii_lowercase # 영어 대문자, 영어 소문자 리스트 만드는 패키지


def solution(my_string):
    answer = 0
    alphabet_uppercase = list(ascii_uppercase)
    alphabet_lowercase = list(ascii_lowercase)

    for i in my_string:
        if i in ascii_uppercase:
            my_string = my_string.replace(i, ' ') # 영어 대문자 지우기
        elif i in ascii_lowercase:
            my_string = my_string.replace(i, ' ') # 영어 소문자 지우기
    print(my_string)
    
    my_string = my_string.split(' ') # ' ' 기준으로 나누어서 리스트로 만들기
    print(my_string)
    
    for j in range(len(my_string)):
        if my_string[j] != '' : # split을 할 경우, 리스트 안에는 ''와 숫자만 남게 됨. => 리스트의 j번째가 공백이 아닐 경우(=숫자일 경우), 그 값을 answer에 더해준다.
            print(my_string[j])
            answer += int(my_string[j])
    
    
    return answer