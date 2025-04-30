from itertools import combinations

def 소수(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    count = 0
    for i in combinations(nums, 3):
        if 소수(sum(i)):
            print(sum((i)))
            count += 1 
    return count