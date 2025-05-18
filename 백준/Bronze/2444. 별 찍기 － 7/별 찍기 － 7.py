import sys

input = sys.stdin.readline

숫자 = int(input())

for i in range(1, 숫자 + 1):
    print(" " * (숫자 - i) + "*" * (2 * i - 1))

for i in range(숫자 - 1, 0, -1):
    print(" " * (숫자 - i) + "*" * (2 * i - 1))
