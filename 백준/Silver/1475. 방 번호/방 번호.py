import sys

from io import StringIO

import math

input = sys.stdin.readline


answer = list(map(int, input().strip()))

누적 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in answer:
    누적[i] += 1


누적[6] = math.ceil((누적[6] + 누적[9]) / 2)

print(max(누적[:9]))
