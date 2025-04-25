def solution(name, yearning, photo):
    answer = []
    짝 = {}
    for i in range(len(name)):
        짝[name[i]] = yearning[i]
    
    for j in range(len(photo)):
        score = 0
        for k in range(len(photo[j])):
            score += (짝.get(photo[j][k], 0))
        answer.append(score)
    return answer