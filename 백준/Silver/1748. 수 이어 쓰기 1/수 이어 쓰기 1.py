import sys
from io import StringIO

input = sys.stdin.readline

N = int(input())
answer = 0


def 자리수합(N):
    answer = 0
    총자리수 = len(str(N))

    for i in range(1, 총자리수 + 1):
        if i == 총자리수:
            answer += i * (N - (pow(10, i - 1) - 1))
        else:
            answer += i * ((pow(10, i) - 1) - (pow(10, i - 1) - 1))

    return answer


print(자리수합(N))
