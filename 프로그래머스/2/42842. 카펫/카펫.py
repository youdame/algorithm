import math
def solution(brown, yellow):
    
    sum = brown + yellow
    
    pairs = []
    for i in range(1, int(math.sqrt(sum)) + 1):
        if sum % i == 0:
            pairs.append((sum // i, i))
    # print(pair)
    
    for col, row in pairs:
        result = 2 * col + 2 * (row - 2)
        if result == brown:
            return [col, row]