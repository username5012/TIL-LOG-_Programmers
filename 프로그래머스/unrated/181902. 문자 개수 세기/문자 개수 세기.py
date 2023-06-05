from string import ascii_uppercase, ascii_lowercase

def solution(my_string):
    answer = []
    upper = list(ascii_uppercase)
    lower = list(ascii_lowercase)
    
    for i in range (26):
        answer += [my_string.count(upper[i])]
    for j in range (26):
        answer += [my_string.count(lower[j])]
    return answer