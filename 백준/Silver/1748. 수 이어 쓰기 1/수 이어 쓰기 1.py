import sys
from io import StringIO

input = sys.stdin.readline

N = int(input())
answer = 0


def 자리수합(N):
    answer = 0
    # 마지막자리수 = N % 10
    # print(마지막자리수)
    # answer += 마지막자리수

    총자리수 = len(str(N))
    for i in range(1, 총자리수 + 1):
        answer += i * ((pow(10, i) - 1) - (pow(10, i - 1) - 1))

    answer -= (pow(10, 총자리수) - 1 - N) * (총자리수)

    return answer


print(자리수합(N))
