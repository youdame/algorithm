from collections import deque
def solution(bandage, health, attacks):
    
    t, x, y = bandage
    
    time = 0 
    max_health = health

    
    for 공격시간, 피해량 in attacks:
        continous_success = 0
        while time < 공격시간:
            
            continous_success += 1
            
            if continous_success == t:
                # print("__")
                health = min(max_health, health + y)
                continous_success = 0
            
            health = min(max_health, health + x)
            # print(time, health, continous_success)
            time += 1
        health -= 피해량
        if health <= 0:
            return -1 
        # print(time, health)
        time += 1
        
    return health 