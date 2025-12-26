import sys
from io import StringIO


input = sys.stdin.readline
n, m = list(map(int, input().strip().split(" ")))
parents = list(map(int, input().strip().split(" ")))
for index in range(len(parents)):
    parents[index] -= 1

score = [0] * n
for i in range(m):
    i, w = list(map(int, input().strip().split(" ")))
    score[i - 1] += w
real_score = [0] * n

for i in range(1, n):
    real_score[i] += real_score[parents[i]] + score[i]
print(*real_score)
