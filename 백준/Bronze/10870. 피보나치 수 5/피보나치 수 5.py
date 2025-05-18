import sys

from io import StringIO


input = sys.stdin.readline


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 2) + fibo(n - 1)


숫자 = int(input())

print(fibo(숫자))
