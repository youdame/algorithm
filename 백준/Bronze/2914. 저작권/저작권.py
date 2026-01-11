import math
import sys
from io import StringIO


input = sys.stdin.readline
A, I = map(int, input().split())




answer = math.ceil(I - 1) * A
print(answer + 1)