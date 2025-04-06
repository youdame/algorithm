def solution(t, p):
    arr = []
    길이 = len(p)
    for i in range(len(t) - 길이 + 1):
        arr.append(t[i:길이 + i])

    count = 0
    for i in arr:
        if(int(i) <= int(p)):
            count+=1
    return count