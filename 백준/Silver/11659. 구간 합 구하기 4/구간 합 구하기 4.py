import sys
from io import StringIO

input = sys.stdin.readline
N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))


psum = [arr[0]]
for i in range(1, N):
    psum.append(psum[i - 1] + arr[i])


for i in range(M):
    a, b = list(map(int, input().split()))

    if a - 2 < 0:
        print(psum[b - 1] - 0)
        continue
    print(psum[b - 1] - psum[a - 2])
