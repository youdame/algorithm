import sys
from io import StringIO


input = sys.stdin.readline

N = int(input())

record = {}
남은시간 = []
점수들 = []
index = 0
for i in range(N):
    arr = list(map(int, input().split()))

    if arr[0]:
        과제나옴, A, T = arr

        남은시간.append(T - 1)
        점수들.append(A)
        index += 1
    else:
        # 이전 과제 중 남은 시간이 0이 아닌 애
        이전인덱스 = index - 1
        while 이전인덱스 >= 0:
            if 남은시간[이전인덱스] > 0:
                남은시간[이전인덱스] -= 1
                break
            else:
                이전인덱스 -= 1
score = 0
for time in range(len(남은시간)):
    if 남은시간[time] == 0:
        score += 점수들[time]
print(score)
