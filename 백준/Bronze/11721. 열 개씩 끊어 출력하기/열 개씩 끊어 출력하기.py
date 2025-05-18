import sys

input = sys.stdin.readline

인풋 = input().strip()

for i in range(0, len(인풋), 10):
    print(인풋[i : 10 + i])
