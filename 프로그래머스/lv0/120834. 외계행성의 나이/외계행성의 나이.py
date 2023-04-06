def solution(age):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    age = str(age)
    print(age)
    for i in alphabet:
        idx = alphabet.index(i)
        if str(idx) in age:
            age = age.replace(str(idx), alphabet[idx])
    
    return age