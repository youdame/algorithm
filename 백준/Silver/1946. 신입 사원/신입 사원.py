import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    지원자등수 = []

    N = int(input())
    선발가능인원 = N
    for j in range(N):
        지원자등수.append(list(map(int, input().strip().split(" "))))
    지원자등수.sort()
    내앞지원자중가장높은등수 = 지원자등수[0][1]
    for index in range(len(지원자등수)):
        서류 = 지원자등수[index][0]
        면접 = 지원자등수[index][1]
        if 내앞지원자중가장높은등수 < 면접:
            선발가능인원 -= 1
        if 내앞지원자중가장높은등수 > 면접:
            내앞지원자중가장높은등수 = 면접
    print(선발가능인원)
    #
    # for index in range(len(면접등수)):
    #     내등수 = 면접등수[index]
    #     if index > 0:
    #         남들등수 = 면접등수[:index]
    #         if 내등수 > min(남들등수):
    #             선발가능인원 -= 1
    # print(선발가능인원)
