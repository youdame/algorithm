import sys
from io import StringIO
from collections import defaultdict


input = sys.stdin.readline
N, M = map(int, input().split())
costs = []
for i in range(N):
    costs.append(int(input()))
votes = defaultdict(int)


for i in range(M):
    기준 = int(input())

    for j in range(N):
        if costs[j] <= 기준:
            votes[j + 1] += 1
            break
max_votes = max(votes.values())
for key, value in votes.items():
    if value == max_votes:
        print(key)
        break
