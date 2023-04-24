

def solution(nums):
    answer = 0
    
    species = list(set(nums))

    
    print(species)
    
    if len (species) > len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = len (species)
    
    
    return answer