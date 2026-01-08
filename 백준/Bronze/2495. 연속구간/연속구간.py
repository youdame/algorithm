import sys
from io import StringIO

input = sys.stdin.readline


추가될점수 = 1
총점수 = 0
for i in range(3):

    arr = list(map(int, list(input().strip())))
    max_연속_길이 = 1
    연속길이 = 1
    for i in range(1, len(arr)):
        if arr[i - 1] == arr[i]:
            연속길이 += 1
        else:
            연속길이 = 1
        max_연속_길이 = max(max_연속_길이, 연속길이)

    print(max_연속_길이)
