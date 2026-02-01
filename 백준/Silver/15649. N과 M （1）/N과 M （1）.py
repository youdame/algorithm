import sys
from io import StringIO
from itertools import permutations


input = sys.stdin.readline

N, M = map(int, input().split())

for comb in permutations(list(range(1,N+1)), M):
    print(" ".join(map(str, comb)))