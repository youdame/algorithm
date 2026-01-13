import sys
from io import StringIO
from itertools import combinations


input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

sum_set = set()
for i in range(1, N + 1):
    for combination in combinations(arr, i):
        sum_set.add(sum(combination))

answer = 0
j = 1
while True:
    if j in sum_set:
        j += 1
    else:
        break

print(j)
