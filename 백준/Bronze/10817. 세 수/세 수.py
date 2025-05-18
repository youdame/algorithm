import sys


input = sys.stdin.readline

배열 = list(map(int, input().split()))
배열.sort()
print(배열[1])
