import sys
from io import StringIO
from itertools import combinations


input = sys.stdin.readline

T = int(input())


arr = [list(map(int, input().split())) for i in range(T)]
n = len(arr) // 2

후보들 = list(range(0, T))

min_gap = 1e9
for b in combinations(후보들, n):
    if 0 in b:
        continue
    a = tuple(sorted([i for i in 후보들 if i not in b]))

    a_score = 0
    b_score = 0
    for comb in combinations(a, 2):
        i, j = comb
        a_score += arr[i][j]
        a_score += arr[j][i]
    for comb in combinations(b, 2):
        i, j = comb
        b_score += arr[i][j]
        b_score += arr[j][i]
    min_gap = min(min_gap, abs(a_score - b_score))
print(min_gap)
