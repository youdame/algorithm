import sys

input = sys.stdin.readline


count = int(input().strip())
for i in range(count, 0, -1):
    print((count - i) * " " + (2 * i - 1) * "*")
