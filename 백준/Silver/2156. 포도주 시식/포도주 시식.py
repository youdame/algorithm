import sys 
from io import StringIO


input = sys.stdin.readline 


N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))


dp = [0] * N

dp[0] = arr[0]



for i in range(1, N):
    if i == 1:
        dp[1] = arr[0] + arr[1]
        continue
    if i == 2:
        dp[2] = max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2])
        continue
    # i-2 X, i-1 O, i O -> dp[i-3] + arr[i-1] + arr[i]
    # i-2 O, i-1 X, i O -> dp[i-2] + arr[i]
    # i X -> dp[i-1]
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1])
print(max(dp))