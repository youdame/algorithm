import sys
from io import StringIO

input = sys.stdin.readline

n = int(input())
arr = []
S = n // 3


print((S - 1) * (S - 2) // 2)
