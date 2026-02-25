def solution(bandage, health, attacks):
    current_health = health
    attack_times = attacks[-1][0]
    attack_index = 0
    
    시전시간, 초당회복량, 추가회복량 = bandage
    double = -1
    for time in range(attack_times+1):
        if attacks[attack_index][0] == time:
            current_health -= attacks[attack_index][1]
            attack_index += 1
            double = 0
        else:
            current_health = min(초당회복량 + current_health, health)
            double += 1
            if double == 시전시간:
                current_health = min(추가회복량 + current_health, health)
                double = 0

        
        if current_health <= 0:
            return -1

    return current_health
    
    
    