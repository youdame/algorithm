import sys
from io import StringIO


input = sys.stdin.readline

T = int(input())

meetings = [tuple(map(int, input().split())) for _ in range(T)]


meetings.sort(key=lambda x: (x[1], x[0]))


answer = 0
answer_end = 0
for meeting in meetings:
    start, end = meeting
    if start < answer_end:
        continue
    else:
        answer_end = end
        answer += 1

print(answer)
