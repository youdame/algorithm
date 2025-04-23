def solution(food):
    answer = ""
    first = ""
    for i in range(len(food)):
        first = (food[i] // 2) * str(i)
        answer += first
    second = answer[::-1]
    answer = answer + "0" + second
    return answer