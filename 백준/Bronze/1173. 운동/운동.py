import sys
from io import StringIO

input = sys.stdin.readline

N, m, M, T, R = list(map(int, input().split()))

time = 0


X = m
if X + T > M:
    print(-1)
    sys.exit()
while N > 0:
    time += 1

    # 운동
    if X + T <= M:
        N -= 1
        X = X + T
    # 휴식
    else:
        if X - R < m:
            X = m
        else:
            X = X - R
print(time)
