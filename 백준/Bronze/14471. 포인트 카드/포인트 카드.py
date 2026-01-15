import sys
from io import StringIO


input = sys.stdin.readline

N, M = list(map(int, input().split()))

경품 = 0
arr = []
for i in range(M):
    A, B = list(map(int, input().split()))
    if A >= N:
        경품 += 1
    else:
        arr.append(N - A)

arr = sorted(arr)
비용 = 0
i = 0
while 경품 < M - 1:
    비용 += arr[i]
    경품 += 1
    i += 1

print(비용)
