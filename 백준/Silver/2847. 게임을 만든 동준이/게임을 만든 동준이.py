import sys
from io import StringIO



input = sys.stdin.readline

N = int(input())

arr = [int(input()) for i in range(N)]
count = 0
# print(arr)
# 맨 뒤 숫자는 고정되어 있으며, 1씩 차이가 난다
for index in range(len(arr) - 1, 0, -1):
    차이 = arr[index] - arr[index - 1]
    # print(arr[index], arr[index - 1])
    # print(차이)
    if 차이 <= 0:
        count += abs(차이) + 1
        arr[index - 1] = arr[index] - 1
    # print(arr)
print(count)
