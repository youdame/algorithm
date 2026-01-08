import sys
from io import StringIO


input = sys.stdin.readline


A, B, C, M = list(map(int, input().split()))

피로도 = 0
일의양 = 0
for _ in range(24):
    if 피로도 + A <= M:
        피로도 += A
        일의양 += B

    else:  # 쉬었을떄
        피로도 -= C
        if 피로도 < 0:
            피로도 = 0
print(일의양)
