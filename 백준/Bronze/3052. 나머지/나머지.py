import sys
from io import StringIO

input = sys.stdin.readline
a = set()
for i in list(map(int, [input() for _ in range(10)])):
    a.add(i % 42)
print(len(a))
