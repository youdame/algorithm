import sys
from io import StringIO

input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split()))
answer_arr = []
record = dict()

answer = 0
for index in range(N):
    if arr[index] not in record:
        record[arr[index]] = 1
    else:
        while record[arr[index]] >= K:
            record[answer_arr.pop(0)] -= 1
        record[arr[index]] += 1

    answer_arr.append(arr[index])

    answer = max(answer, len(answer_arr))
print(answer)
