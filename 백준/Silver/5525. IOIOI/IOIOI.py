import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

answer = 0
cnt = 0
i = 0

while i < M - 2:
    if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == 'I':
        cnt += 1
        if cnt >= N:
            answer += 1
        i += 2      # 겹치게 허용
    else:
        cnt = 0
        i += 1

print(answer)