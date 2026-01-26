import sys
from io import StringIO


input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
answer = 0

psum = [arr[0]]

for i in range(1, N):
    psum.append(psum[i - 1] + arr[i])

for j in range(1, N):
    answer += 2 * (arr[j] * j - psum[j - 1])
print(answer)
