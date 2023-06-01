def solution(my_string, queries):
    my_string = list(my_string)
    
    for query in queries:
        s,e = query[0], query[1]
        opposite = my_string[s:e+1]
        opposite.reverse()
        my_string[s:e+1] = opposite
        
        
        
        
        
    
    my_string = ''.join(my_string)
    
    return my_string