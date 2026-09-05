from collections import Counter

def solution(topping):

    split_dot = 0
    n = len(topping)
    
    
    set1 = set(topping[:split_dot])
    set2 = Counter(topping[split_dot:])
    
    count1 = len(set1)
    count2 = len(set2.keys())
    answer = 0
    # print(set1, set2.keys())
    
    while split_dot < n:
        new_topping = topping[split_dot]
        
        if new_topping not in set1:
            count1 += 1
            set1.add(new_topping)
        
        set2[new_topping] -= 1
        
        if not set2[new_topping] :
            count2 -= 1
        if count1 == count2:
            answer += 1
            
        split_dot += 1
        
        # print(count1, count2)
    return answer