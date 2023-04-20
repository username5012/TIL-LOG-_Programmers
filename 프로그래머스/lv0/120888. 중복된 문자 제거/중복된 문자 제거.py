def solution(my_string):
    answer = ''
    string_1 = list(dict.fromkeys(my_string))
    answer = "".join(string_1)
    return answer