def solution(arr1, arr2):
    answer = []
    rows = len(arr1)
    columns = len(arr1[0])
    
    for row in range(rows):
        make_list = []       
        for column in range(columns):
            make_list += [arr1[row][column] + arr2[row][column]]
        answer += [make_list]
        
            
    return answer