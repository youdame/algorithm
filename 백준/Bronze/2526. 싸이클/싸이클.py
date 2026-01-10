import sys
from io import StringIO


input = sys.stdin.readline


cycle_start_number = 0
N, P = map(int, input().split())
answer = [N, (N * N) % P]
while True:
    구한값 = answer[-1] * N % P

    if 구한값 in answer:
        cycle_start_number = 구한값
        break
    answer.append(구한값)

print(len(answer[answer.index(구한값) :]))
