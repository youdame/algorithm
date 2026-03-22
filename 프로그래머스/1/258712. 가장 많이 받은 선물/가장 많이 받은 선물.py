from collections import defaultdict
def solution(friends, gifts):
    # 기록 중 더 적게 준 사람이 더 많이 준 사람에게 선물
    # 주고 받은 기록이 없거나, 똑같이 주고 받았으면 선물지수 구하기 선물지수 낮은 사람 -> 높은 사람 
    # 서로 주고 받은 기록 
    record = {friend : {g : 0 for g in friends if friend != g} for friend in friends}
    
    # 내 기준 주고 받은 기록 
    given_record = {friend : 0 for friend in friends}
    taken_record = {friend : 0 for friend in friends}
    
    for gift in gifts:
        giver, taker = gift.split()
        record[giver][taker] += 1
        given_record[giver] += 1
        taken_record[taker] += 1
    
    선물지수 = {}
    for f in friends:
        선물지수[f] = given_record[f] - taken_record[f]

    
    answer = defaultdict(int)
    for me in friends:
        for other in friends:
            if me == other:
                continue
            else:
                if record[me][other] > record[other][me]:
                    answer[me] += 1
                elif record[me][other] == record[other][me] or (record[me][other] == record[other][me] == 0) :
                    if 선물지수[me] > 선물지수[other]:
                        answer[me] += 1
    print(answer)
    
    max_value = 0
    
    for key, value in answer.items():
        max_value = max(value, max_value)
    return max_value
                    
            