def solution(n):
    
    arr = list(str(n))
    arr.sort(reverse = True)
    return int("".join(arr))
# def solution(n):
#     ls = list(str(n))
#     ls.sort(reverse = True)
#     return int("".join(ls))
