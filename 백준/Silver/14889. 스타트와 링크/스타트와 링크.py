import sys
from io import StringIO
from itertools import combinations



input = sys.stdin.readline

T = int(input())


arr = [list(map(int, input().split())) for i in range(T)]
n = len(arr) // 2

후보들 = list(range(1, T + 1))
seen = set()

min_gap = 1e9
for b in combinations(후보들, n):
    a = tuple(sorted([i for i in 후보들 if i not in b]))
    if a not in seen:
        seen.add(b)
    else:
        continue

    a_score = 0
    b_score = 0
    for comb in combinations(a, 2):
        i, j = comb
        a_score += arr[i - 1][j - 1]
        a_score += arr[j - 1][i - 1]
    for comb in combinations(b, 2):
        i, j = comb
        b_score += arr[i - 1][j - 1]
        b_score += arr[j - 1][i - 1]
    min_gap = min(min_gap, abs(a_score - b_score))
print(min_gap)
