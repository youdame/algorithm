from collections import defaultdict
def solution(clothes):
    record = defaultdict(list)
    for name, category in clothes:
        record[category].append(name)
    
    answer = 1
    
    for key in record.keys():
        # print(record[key])
        answer *= len(record[key]) + 1
    # print(answer)
    return answer - 1