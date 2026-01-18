import sys
from io import StringIO

input = sys.stdin.readline

N, K = map(int, input().split())


arr = list(input().strip())


eaten = [False] * N
for i in range(N):
    if arr[i] == "P":
        for j in range(i - K, i + K + 1):
            if 0 <= j <= N - 1 and arr[j] == "H" and not eaten[j]:
                eaten[j] = True
                break
print(eaten.count(True))
