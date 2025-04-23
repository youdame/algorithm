def solution(a, b, n):
    bonus = 0
    current = n

    while True:
        몫 = (current // a) 
        나머지 = current % a
        bonus += 몫 * b 
        current = 몫 * b
        current += 나머지    
        print(current, bonus)
        if current < a:
            return bonus
