import sys 
from io import StringIO

input = sys.stdin.readline

count = [0] * 10001

N = int(input())

for _ in range(N):
    num = int(input())
    count[num] += 1

for i in range(1, 10001):
    for j in range(count[i]):
        print(i)