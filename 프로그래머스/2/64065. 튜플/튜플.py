def solution(s):
    n = len(s)

    answer = []
    arr = []
    for element in s[2:n-2].split("},{"):
        arr.append(list(map(int, element.split(','))))
    arr.sort(key = lambda x : len(x))
    
    for element in arr:
        answer.extend(element)
    
    result = []
    
    for element in answer:
        if element not in result:
            result.append(element)
    return result
    