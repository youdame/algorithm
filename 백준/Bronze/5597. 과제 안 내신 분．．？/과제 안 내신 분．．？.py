import sys
from io import StringIO

input = sys.stdin.readline


arr = [0] * 30

for i in range(28):
    arr[int(input()) - 1] = 1

for answer in [i + 1 for i in range(len(arr)) if arr[i] == 0]:
    print(answer)
