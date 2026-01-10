import sys
from io import StringIO


input = sys.stdin.readline
N = int(input())

record = {}


needs = list(map(int, input().split()))
reals = list(map(int, input().split()))

for index in range(N):
    need = needs[index]
    if need in record:
        record[needs[index]] += 1
    else:
        record[needs[index]] = 1
answer = 0
for real in reals:
    if real in record and record[real] > 0:
        record[real] -= 1
    else:
        answer += 1

print(answer)
