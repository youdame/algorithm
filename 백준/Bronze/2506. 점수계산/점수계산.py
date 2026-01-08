import sys
from io import StringIO


input = sys.stdin.readline


N = int(input())
ox_arr = list(map(int, input().split()))


추가될점수 = 1
총점수 = 0
for i in range(len(ox_arr)):

    if ox_arr[i]:
        총점수 += 추가될점수
        추가될점수 += 1
    else:
        추가될점수 = 1
print(총점수)
