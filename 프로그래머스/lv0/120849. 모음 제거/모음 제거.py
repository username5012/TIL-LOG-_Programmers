def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for alp in vowels:
        print(alp)
        if alp in my_string:
            my_string = my_string.replace(alp,'')
    return my_string