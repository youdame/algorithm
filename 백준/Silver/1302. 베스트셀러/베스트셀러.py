import sys
from io import StringIO

input = sys.stdin.readline

N = int(input())
record = {}

for i in range(N):
    name = input().strip()
    if name in record:
        record[name] += 1
    else:
        record[name] = 1

max_value = max(record.values())

answer = []

for name, value in record.items():
    if value == max_value:
        answer.append(name)

answer.sort()
print(answer[0])
