def solution(spell, dic):
    answer = 2
    
    spell = set(spell)

    for i in dic:
        if list(spell-set(i)) == []:
            print('True :', 'spell =', spell, '| set(i) =', set(i))
            answer = 1
        
        if answer == 1:
            for j in spell:
                if i.count(j) > 1:
                    print('except :', 'spell =', spell, '| set(i) =', list(i), "| except =", j)
                    print(j)
                    answer = 2

                    
    return answer
    