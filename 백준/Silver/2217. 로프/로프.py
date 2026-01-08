import sys
from io import StringIO

input = sys.stdin.readline


N = int(input())
로프들 = sorted([int(input()) for i in range(N)])



최대중량 = 로프들[0] * N

for i in range(N):
    if 최대중량 < 로프들[i] * (N - i):
        최대중량 = 로프들[i] * (N - i)
print(최대중량)
