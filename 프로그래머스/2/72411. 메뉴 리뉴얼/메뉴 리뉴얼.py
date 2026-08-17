"""
함께 많이 주문한 단품 메뉴를 코스 요리로 구성
코스 메뉴
- 2가지 이상의 단품 메뉴
- 2명 이상의 손님으로부터 주문된 단품 메뉴 조합만 포함

"""

from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    set_collection = []
    record = defaultdict(int)
    
    
    orders = ["".join(sorted(order)) for order in orders]
    
    for num in course:
        for order in orders:
            for comb in combinations(order, num):
                record[comb] += 1
                
    
    answer = []
    for num in course:
        max_key = ""
        max_value = -1e9
        
        for key, value in record.items():
            if len(key) == num and value > max_value and value >= 2:
                max_value = value
                max_key = key
        
        if max_value != -1e9:
            answer.append(max_key)
            
        for key, value in record.items():
            if len(key) == num and max_value == value and key not in answer:
                answer.append(key)
    answer = sorted(["".join(element) for element in answer])
    return (answer)

    