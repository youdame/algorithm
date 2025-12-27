import sys
from io import StringIO

input = sys.stdin.readline

N = int(input())

if N % 5 == 0:
    print(N // 5)
    sys.exit()
else:
    # 5로만 불가능한 경우 , 2를 몇 개 쓰면 될까요?
    이원개수 = 0
    while N != 0:
        if N < 0:
            print(-1)
            sys.exit()
        이원개수 += 1
        N = N - 2
        if N % 5 == 0:
            오원개수 = N // 5
            break
print(이원개수 + 오원개수)
