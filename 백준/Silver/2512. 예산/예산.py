import sys

input = sys.stdin.readline
N = int(input())

answer = 0
예산요청 = list(map(int, input().strip().split(" ")))
국가예산 = int(input())


def 조건만족(상한액):
    실제배정 = 0
    for 요청 in 예산요청:
        실제배정 += min(상한액, 요청)
    return 실제배정 <= 국가예산


if sum(예산요청) <= 국가예산:
    print(max(예산요청))
else:
    left = 0
    right = max(예산요청)

    while left <= right:
        mid = (left + right) // 2
        if 조건만족(mid):
            answer = mid
            left = mid + 1

        else:
            right = mid - 1
    print(answer)
