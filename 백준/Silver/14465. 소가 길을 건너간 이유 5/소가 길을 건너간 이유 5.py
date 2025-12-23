import sys
from io import StringIO




input = sys.stdin.readline

N, K, B = list(map(int, input().strip().split(" ")))

arr = [int(input()) for i in range(B)]

신호등 = [1] * N

for 고장 in arr:
    신호등[고장 - 1] = 0
psum = []
psum.append(sum(신호등[:K]))

for i in range(1, N - K + 1):
    psum.append(psum[i - 1] + 신호등[i + K - 1] - 신호등[i - 1])
print(K - max(psum))
