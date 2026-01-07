import sys
from io import StringIO
from itertools import combinations


input = sys.stdin.readline


N = int(input())
for i in range(N):
    for word in input().strip().split():
        print(word[::-1], end=" ")
    print("")
