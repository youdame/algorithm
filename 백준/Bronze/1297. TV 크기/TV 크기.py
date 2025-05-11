import sys

import math


input = sys.stdin.readline

대각선, 높이, 너비 = map(int, input().split(" "))

x = math.sqrt(대각선 **2 / (너비 **2 + 높이 ** 2))
print(int(높이  * x), int(너비*x))