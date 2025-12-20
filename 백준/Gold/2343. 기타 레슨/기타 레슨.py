import sys


input = sys.stdin.readline
N, M = list(map(int, input().split(" ")))
영상들 = list(map(int, input().split(" ")))
전체영상들용량합 = sum(영상들)
left = max(영상들)
right = 전체영상들용량합
answer = 0


def 조건만족(value):

    블루레이수 = 1
    현재블루레이용량 = 0

    for 영상 in 영상들:
        if 현재블루레이용량 + 영상 <= value:
            현재블루레이용량 += 영상
        else:
            블루레이수 += 1
            현재블루레이용량 = 영상
    if 블루레이수 <= M:
        return True
    return False


while left <= right:
    mid = (left + right) // 2
    if 조건만족(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)
