import sys
from io import StringIO


input = sys.stdin.readline
N, T = list(map(int, input().split()))

팔개수 = 1
증가여부 = True
for _ in range(T - 1):

    if 팔개수 == 2 * N:
        증가여부 = False
    elif 팔개수 == 1:
        증가여부 = True

    if 증가여부:
        팔개수 += 1
    else:
        팔개수 -= 1

print(팔개수)
