def solution(d, budget):
    sum = 0
    d.sort()
    for i in range(len(d)):
        sum += d[i]
        print(i, "sum",sum)
        if(sum > budget):
            return i 
    if sum <= budget:
        return len(d)
    