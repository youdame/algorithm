import sys
from io import StringIO


input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


psum = [arr[0]]
for i in range(1, n):
    psum.append(psum[i-1] + arr[i])


# 앞의 연속 수열에 나를 붙일지 or 여기서 새로 시작할지

dp = [arr[0]]


for i in range(1, n):
    case_1 = dp[i-1] + psum[i] - psum[i-1]
    case_2 = psum[i] - psum[i-1]
    
    dp.append(max(case_1, case_2))
print(max(dp))

