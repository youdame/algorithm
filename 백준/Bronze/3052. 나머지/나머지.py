import sys


input = sys.stdin.readline

배열 = []
for i in range(10):
  배열.append(int(input()) % 42)

print(len(set(배열)))
