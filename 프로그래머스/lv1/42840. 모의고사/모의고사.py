def solution(answers):
    answer = []
    
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    answer_count = [0,0,0]
    
    for num in range(len(answers)):
        if answers[num] == first[num%len(first)]:
            print('correct_first : ', num, answers[num])
            answer_count[0] += 1
        
        if answers[num] == second[num%len(second)]:
            print('correct_second : ', num, answers[num])
            answer_count[1] += 1
            
        if answers[num] == third[num%len(third)]:
            print('correct_third : ', num, answers[num])
            answer_count[2] += 1
        
    
    
    for person, cnt in enumerate(answer_count):
        if cnt == max(answer_count):
            answer += [person+1]
    
    
    
    return answer