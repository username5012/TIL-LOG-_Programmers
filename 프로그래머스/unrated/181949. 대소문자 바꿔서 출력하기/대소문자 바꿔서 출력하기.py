from string import ascii_uppercase, ascii_lowercase

str = input()
answer = ''

upper = list(ascii_uppercase)
lower = list(ascii_lowercase)

for i in range(len(str)):
    a = str[i]
    if a in upper:
        answer += a.lower()
    elif a in lower:
        answer += a.upper()
    

print(answer)

    
