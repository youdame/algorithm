import sys


input = sys.stdin.readline

a, b = map(int, input().split(" "))
c, d = map(int, input().split(" "))

print(min(b + c, a + d))
