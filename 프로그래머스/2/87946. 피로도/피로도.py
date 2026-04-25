from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for per in permutations(dungeons):        
        hp = k
        count = 0 
        for 필요, 소모 in per:
            if 필요 <= hp:
                hp -= 소모
                count +=1 
            if hp <= 0:
                break
        answer = max(count, answer)
        # print(answer)
    return answer
    