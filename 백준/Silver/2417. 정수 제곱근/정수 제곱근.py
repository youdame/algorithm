import math
import sys
from io import StringIO

input = sys.stdin.readline

N = int(input())
x = math.isqrt(N)
print(x if x * x >= N else x + 1)
