import sys

from io import StringIO


숫자 = int(input())

for i in range(1, 숫자 + 1):
    print(" " * (숫자 - i) + "*" * (2 * i - 1))
