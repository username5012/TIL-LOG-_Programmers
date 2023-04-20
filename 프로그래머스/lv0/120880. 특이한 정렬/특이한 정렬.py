def solution(numlist, n):
    
    for i in range(len(numlist)):
        for j in range(i+1, len(numlist)):
            if abs(numlist[i]-n) > abs(numlist[j]-n):
                numlist[i], numlist[j] = numlist[j], numlist[i]
            elif abs(numlist[i]-n) == abs(numlist[j]-n):
                if numlist[i]-n < numlist[j]-n:
                    numlist[i], numlist[j] = numlist[j], numlist[i]
        print(numlist)

        
    return numlist