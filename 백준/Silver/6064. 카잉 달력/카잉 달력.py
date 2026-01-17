import sys
from io import StringIO


input = sys.stdin.readline

T = int(input())

for i in range(T):
    M, N, x, y = map(int, input().split())

    k = x
    n = 0
    while True:
        if n == N:
            k = -1
            break

        if (k - 1) % N + 1 == y:
            break
        else:
            k += M
            n += 1

    print(k)
