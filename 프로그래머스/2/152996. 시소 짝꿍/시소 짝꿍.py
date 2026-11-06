from bisect import bisect_left, bisect_right

def solution(weights):
    weights.sort()
    # print(weights)
    n = len(weights)
    answer = 0 
    for i in range(n):
        weight = weights[i]
        answer += bisect_right(weights, weight, i+1) -  bisect_left(weights, weight, i+1)
        answer += bisect_right(weights, weight*(3/2), i+1) -  bisect_left(weights, weight*(3/2), i+1)
        answer += bisect_right(weights, weight*2, i+1) -  bisect_left(weights, weight*2, i+1)
        answer += bisect_right(weights, weight*(4/3), i+1) -  bisect_left(weights, weight*(4/3), i+1)
    return answer
        