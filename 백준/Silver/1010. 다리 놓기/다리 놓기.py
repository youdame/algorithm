import sys
from io import StringIO


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    top = 1
    for i in range(m, m-n, -1):
        top *= i

    bottom = 1
    for i in range(n, 1, -1):
        bottom *= i

    print(top // bottom)