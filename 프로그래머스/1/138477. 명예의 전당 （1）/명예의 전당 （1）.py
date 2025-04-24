def solution(k, score) :
    result = []
    answer = []
    for i in range(len(score)):
        if i < k:
            answer.append(score[i])
        elif min(answer) < score[i] :
            answer.remove(min(answer))
            answer.append(score[i])
        result.append(min(answer))
    return result
        
