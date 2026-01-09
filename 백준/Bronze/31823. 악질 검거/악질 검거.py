import sys
from io import StringIO

input = sys.stdin.readline


N, M = map(int, input().split())

dict = {}
for i in range(N):

    인풋 = input().strip().split()
    records = 인풋[: len(인풋) - 1]
    name = 인풋[-1]
    max_count = 0
    count = 0

    for record in records:
        if record == ".":
            count += 1
        elif record == "*":
            count = 0
        max_count = max(count, max_count)
    dict[name] = max_count

print(len(set(dict.values())))
for key, value in dict.items():
    print(value, key)
