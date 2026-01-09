import sys
from io import StringIO

input = sys.stdin.readline


N = int(input())
막대기들 = [int(input()) for i in range(N)][::-1]
max_value = -1
count = 0
for index in range(N):
    if max_value < 막대기들[index]:
        max_value = max(max_value, 막대기들[index])
        count += 1
print(count)
