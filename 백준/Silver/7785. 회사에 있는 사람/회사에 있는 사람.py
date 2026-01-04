import sys
from io import StringIO


input = sys.stdin.readline

N = int(input())
record = {}
for i in range(N):
    name, status = input().split()
    if status == "enter":
        record[name] = 1
    else:
        record[name] = 0

answer = []
for name, count in record.items():
    if count == 1:
        answer.append(name)
for name in sorted(answer, reverse=True):
    print(name)
