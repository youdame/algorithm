def solution(arr, divisor):
    list = []
    for element in arr:
        if element % divisor == 0:
            list.append(element)
    if(len(list) == 0):
        return [-1]
    list.sort()
    return list