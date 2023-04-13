def slope (x1, y1, x2, y2):
    bias = (y2 - y1) / (x2 - x1)
    print("y증가량:", y2-y1)
    print("x증가량:", x2-x1)
    print(bias)
    
    return bias

def solution(dots):
    answer = 0
    
    A = dots[0]
    B = dots[1]
    C = dots[2]
    D = dots[3]
    
#     print(A[0], A[1])
#     print(B[0], B[1])
#     print(C[0], C[1])
#     print(D[0], D[1])
    
#     print("a-b", slope(A[0], A[1], B[0], B[1]))
#     print("c-d", slope(C[0], C[1], D[0], D[1]))
    
#     print("a-c", slope(A[0], A[1], C[0], C[1]))
#     print("b-d", slope(B[0], B[1], D[0], D[1]))
    
#     print("a-d", slope(A[0], A[1], D[0], D[1]))
#     print("c-b", slope(C[0], C[1], B[0], B[1]))
    
    
    
    
    
    
    # A-B C-D
    if slope(A[0], A[1], B[0], B[1]) == slope (C[0],C[1], D[0], D[1]):
        answer = 1
    
    # A-C B-D
    if slope(A[0], A[1], C[0], C[1]) == slope (B[0],B[1], D[0], D[1]):
        answer = 1

    
    # A-D B-C
    if slope(A[0], A[1], D[0], D[1]) == slope (C[0],C[1], B[0], B[1]):
        answer = 1
    
    
    return answer