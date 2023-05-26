def solution(ineq, eq, n, m):
    answer = 0
    icon = ineq + eq
    
    if icon == ">=":
        if n >= m:
            answer = 1
    elif icon == "<=":
        if n <= m:
            answer = 1
    elif icon == ">!":
        if n > m:
            answer = 1
    elif icon == "<!":
        if n < m:
            answer = 1
    return answer