from itertools import combinations
def solution(number):
    lists = list(combinations(number, 3))
    count=0
    for element in lists:
        if sum(element) == 0:
            count+=1
    return count