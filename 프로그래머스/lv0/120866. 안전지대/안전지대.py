from copy import deepcopy

def solution(board):
    
    answer = 0
    
    danger = deepcopy(board)
    print(danger)
    
    for i in range (len(board)):
        for j in range (len(board)):
            if board[i][j] == 1:
                print(i,j)
                if len(board) == 1:
                    pass
                    
                else:
                    if i == 0:
                        if j == 0:
                            danger[i][j] = 1
                            danger[i+1][j] = 1

                            danger[i][j+1] = 1
                            danger[i+1][j+1] = 1
                            
                            print(danger)

                        elif j == len(board)-1:
                            danger[i][j] = 1
                            danger[i+1][j] = 1

                            danger[i][j-1] = 1
                            danger[i+1][j-1] = 1
                            
                            print(danger)


                        else:
                            danger[i][j] = 1
                            danger[i+1][j] = 1

                            danger[i][j-1] = 1
                            danger[i+1][j-1] = 1

                            danger[i][j+1] = 1
                            danger[i+1][j+1] = 1
                            
                            print(danger)



                    elif i == len(board)-1:
                        if j == 0:
                            danger[i-1][j] = 1
                            danger[i][j] = 1

                            danger[i-1][j+1] = 1
                            danger[i][j+1] = 1
                            
                            print(danger)

                        elif j == len(board)-1:
                            danger[i-1][j] = 1
                            danger[i][j] = 1

                            danger[i-1][j-1] = 1
                            danger[i][j-1] = 1
                            
                            print(danger)


                        else:
                            danger[i-1][j] = 1
                            danger[i][j] = 1

                            danger[i-1][j-1] = 1
                            danger[i][j-1] = 1

                            danger[i-1][j+1] = 1
                            danger[i][j+1] = 1
                            
                            print(danger)



                    else:
                        if j == 0:
                            danger[i-1][j] = 1
                            danger[i][j] = 1
                            danger[i+1][j] = 1

                            danger[i-1][j+1] = 1
                            danger[i][j+1] = 1
                            danger[i+1][j+1] = 1
                            print(danger)

                        elif j == len(board)-1:
                            danger[i-1][j] = 1
                            danger[i][j] = 1
                            danger[i+1][j] = 1

                            danger[i-1][j-1] = 1
                            danger[i][j-1] = 1
                            danger[i+1][j-1] = 1
                            print(danger)


                        else:
                            danger[i-1][j] = 1
                            danger[i][j] = 1
                            danger[i+1][j] = 1

                            danger[i-1][j-1] = 1
                            danger[i][j-1] = 1
                            danger[i+1][j-1] = 1

                            danger[i-1][j+1] = 1
                            danger[i][j+1] = 1
                            danger[i+1][j+1] = 1
                            print(danger)
                    
    
    
    for list in danger:
        answer += list.count(0)
    
    return answer



