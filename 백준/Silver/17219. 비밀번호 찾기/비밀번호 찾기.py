import sys
from io import StringIO

input = sys.stdin.readline

N, M = list(map(int, input().split()))
dict = {}
for i in range(N):
    address, password = input().strip().split()
    dict[address] = password
for j in range(M):
    print(dict[input().strip()])
