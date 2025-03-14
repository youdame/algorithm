def solution(x, n):
    answer = []
    item = 0
    while (len(answer) < n):
        item += x 
        answer.append(item)

    return answer