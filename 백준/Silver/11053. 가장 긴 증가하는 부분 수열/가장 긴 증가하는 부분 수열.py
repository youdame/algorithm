import sys 
from io import StringIO

input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N

# i로 끝나는 가장 긴 부분 증가 수열

dp[0] = 1

for i in range(1, N):
    max_value = 0
    for j in range(i):
        if arr[j] < arr[i]:
            max_value = max(max_value, dp[j])
    dp[i] = max_value + 1
print(max(dp))