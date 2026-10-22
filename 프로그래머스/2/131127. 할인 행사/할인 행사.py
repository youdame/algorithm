from collections import defaultdict
"""
["apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",]
"""



def solution(want, number, discount):
    want_counter = {w : n for w , n in zip(want, number)}
    discount_counter = defaultdict(int)
    
    for i in range(10):
        discount_counter[discount[i]] +=1
        
    for i in range(len(want)):
        want_counter[want[i]] = number[i]
    
    def check():
        for k in range(len(want)):
            if want_counter[want[k]] > discount_counter[want[k]]:
                return False
        return True
    
    answer = 1 if check() else 0

    
    for j in range(0, len(discount) - 10):
        discount_counter[discount[j]] -= 1
        discount_counter[discount[j+10]] += 1
        possible = True
        if check():
            answer += 1
    return answer
            
                
        

    