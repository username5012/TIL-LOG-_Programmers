def solution(array, commands):
    answer = []
    
    for command in commands:
        start = command[0] - 1
        end = command[1]
        idx = command[2] - 1
        print(start, end, idx)
        
        copy = array[start:end]
        copy.sort()
        print(copy)
        answer += [copy[idx]]
        
    return answer