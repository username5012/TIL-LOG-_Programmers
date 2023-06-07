def solution(arr, query):
    for idx in range(len(query)):
        i = query[idx]
        if idx % 2 == 0:
            arr = arr[:i+1]
        else:
            arr = arr[i:]
    return arr