import sys
from io import StringIO


input = sys.stdin.readline


n, A, B = list(map(int, input().split()))
answer = 0
while True:
    A = (A + 1) // 2
    B = (B + 1) // 2
    answer += 1
    if A == B:
        break
print(answer)
