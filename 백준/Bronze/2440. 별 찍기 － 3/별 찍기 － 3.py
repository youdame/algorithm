import sys


input = sys.stdin.readline

a = int(input())
for i in range(0, a):
  for j in range(a, i, -1):
    # print(j)
    print("*", end="")
  print()
