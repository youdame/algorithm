import sys
from io import StringIO
from itertools import combinations


input = sys.stdin.readline


N, M = list(map(int, input().split()))
사람별선호도들 = [list(map(int, input().split())) for i in range(N)]

answer = 0
max_value = -1e9
for 치킨집1, 치킨집2, 치킨집3 in list(combinations([i for i in range(M)], 3)):
    value = 0
    for 사람 in range(N):
        value += max(
            사람별선호도들[사람][치킨집1],
            사람별선호도들[사람][치킨집2],
            사람별선호도들[사람][치킨집3],
        )
    if max_value < value:
        max_value = value
print(max_value)
