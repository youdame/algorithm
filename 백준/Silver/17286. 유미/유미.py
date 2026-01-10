import math
import sys
from io import StringIO
from itertools import permutations


input = sys.stdin.readline


유미x, 유미y = map(int, input().split())


record = []
for i in range(3):
    x, y = map(int, input().split())
    record.append((x, y))

min_value = 1e9

for permutation in permutations(record, 3):
    현재 = (유미x, 유미y)
    value = 0
    for x, y in permutation:
        value += math.sqrt(
            (현재[0] - x) * (현재[0] - x) + (현재[1] - y) * (현재[1] - y)
        )
        현재 = (x, y)
    min_value = min(value, min_value)
print(math.floor(min_value))
