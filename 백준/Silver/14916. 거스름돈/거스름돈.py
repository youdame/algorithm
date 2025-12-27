import sys
from io import StringIO

input = sys.stdin.readline

N = int(input())

오원개수 = N // 5
N = N - 오원개수 * 5
이원개수 = N // 2 if N % 2 == 0 else 0
N = N - 이원개수 * 2

while N != 0:
    오원개수 -= 1
    if 오원개수 < 0 and N % 2 != 0:
        print(-1)
        sys.exit()
    N += 5
    이원개수 = N // 2 if N % 2 == 0 else 0

    N = N - 이원개수 * 2


print(오원개수 +  이원개수)
