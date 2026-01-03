import sys
from io import StringIO

input = sys.stdin.readline
N, K = list(map(int, input().split()))
arr = list(map(int, input().split()))
count = 0


psum = [arr[0]]


for i in range(1, N):
    psum.append(psum[i - 1] + arr[i])


count = {}
answer = 0
for i in range(N):
    goal = psum[i] - K
    if goal == 0:
        answer += 1
    if goal in count:
        answer += count[goal]

    if psum[i] not in count:
        count[psum[i]] = 0
    count[psum[i]] += 1
print(answer)
