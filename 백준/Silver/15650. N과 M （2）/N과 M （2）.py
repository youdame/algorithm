import sys
from io import StringIO
from itertools import combinations


input = sys.stdin.readline

N, M = list(map(int, input().split(" ")))

for element in combinations([i for i in range(1, N + 1)], M):
    print(*element)
