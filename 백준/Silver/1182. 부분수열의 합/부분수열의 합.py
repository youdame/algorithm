import sys
from io import StringIO
from itertools import combinations

input = sys.stdin.readline


N, S = list(map(int, input().split()))
arr = list(map(int, input().split()))

answer = 0
for i in range(1, N+1):
    for 조합 in combinations(arr, i):
        if sum(조합) == S:
            answer += 1
print(answer)
