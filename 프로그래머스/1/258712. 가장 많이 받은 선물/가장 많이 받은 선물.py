from collections import defaultdict
def solution(friends, gifts):
    # 기록 중 더 적게 준 사람이 더 많이 준 사람에게 선물
    # 주고 받은 기록이 없거나, 똑같이 주고 받았으면 선물지수 구하기 선물지수 낮은 사람 -> 높은 사람 
    
    # 서로 주고 받은 기록 
    record = {f : {g : 0 for g in friends if f != g} for f in friends}
    
    
    gift_score = defaultdict(int)
    
    for gift in gifts:
        giver, taker = gift.split()
        record[giver][taker] += 1
        gift_score[giver] += 1
        gift_score[taker] -= 1

    
    answer = defaultdict(int)
    
    for me in friends:
        for other in friends:
            if me == other:
                continue
            
            if record[me][other] > record[other][me]:
                answer[me] += 1
            elif record[me][other] == record[other][me]:
                if gift_score[me] > gift_score[other]:
                    answer[me] += 1
    

    return max(answer.values(), default=0)
                    
            