from collections import defaultdict
"""
["apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",]
"""
def solution(want, number, discount):
    want_counter = {}
    discount_counter = defaultdict(int)
    for i in range(len(want)):
        want_counter[want[i]] = number[i]
    for i in range(10):
        discount_counter[discount[i]] +=1
    answer = 0
    possible = True
    for k in range(len(want)):
        if want_counter[want[k]] > discount_counter[want[k]]:
            possible = False
            break
    if possible:
        answer += 1
    


    
    for j in range(0, len(discount) - 10):
        discount_counter[discount[j]] -= 1
        discount_counter[discount[j+10]] += 1
        possible = True
        for k in range(len(want)):
            # print(k, want[k])
            if want_counter[want[k]] > discount_counter[want[k]]:
                possible = False
                break
        if possible:
            answer += 1
    return answer
            
                
        

    