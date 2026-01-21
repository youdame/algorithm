import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))

x.sort()

prefix = [0] * N
prefix[0] = x[0]
for i in range(1, N):
    prefix[i] = prefix[i-1] + x[i]

answer = 0
for i in range(N):
    # 왼쪽
    if i > 0:
        answer += x[i] * i - prefix[i-1]
    # 오른쪽
    answer += (prefix[N-1] - prefix[i]) - x[i] * (N - i - 1)

print(answer)