import sys
from io import StringIO


input = sys.stdin.readline

T = int(input())

paper = [[False] * 100 for _ in range(100)]


answer = 0

for _ in range(T):
    n, m = map(int, input().split())
    for i in range(n, n + 10):
        for j in range(m, m + 10):
            if paper[i][j] == True:
                answer += 1
            else:
                paper[i][j] = True

print(10*10*T- answer)

