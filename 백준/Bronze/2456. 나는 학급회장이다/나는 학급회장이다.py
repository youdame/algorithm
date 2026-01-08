import sys
from io import StringIO


input = sys.stdin.readline


N = int(input())


record = [[0] * 4 for i in range(4)]

for i in range(N):
    후보1점수, 후보2점수, 후보3점수 = list(map(int, input().split()))
    record[1][후보1점수] += 1
    record[2][후보2점수] += 1
    record[3][후보3점수] += 1

records = [(0, 0, 0, 0)]

for j in range(1, 4):
    총점, one_point, two_point, three_point = record[j]
    총점 = 1 * one_point + 2 * two_point + 3 * three_point
    records.append((총점, three_point, two_point, j))
records = sorted(records, reverse=True)
answer = []

if records[0][:2] != records[1][:2]:
    answer.append(records[0][3])
    answer.append(records[0][0])
else:
    answer.append(0)
    answer.append(records[0][0])
print(*answer)
