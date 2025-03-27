def solution(s):
    arr = list(s)
    arr2 = []
    for i in arr:
        if(i == "("):
            arr2.append("(")
        else:
            if(len(arr2) == 0):
                return False
            arr2.pop()
    if len(arr2) == 0:
        return  True
    return False