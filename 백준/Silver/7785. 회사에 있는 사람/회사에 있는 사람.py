import sys
from io import StringIO

input = sys.stdin.readline

N = int(input())
record = set()
for i in range(N):
    name, status = input().split()
    if status == "enter":
        record.add(name)
    else:
        record.remove(name)
for element in sorted(list(record))[::-1]:
    print(element)
