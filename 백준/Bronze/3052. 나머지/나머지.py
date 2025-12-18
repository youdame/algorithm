import sys

input = sys.stdin.readline
arr = [0] * 42
for i in list(map(int, [input() for _ in range(10)])):
    arr[i % 42] = 1
print(sum(arr))
