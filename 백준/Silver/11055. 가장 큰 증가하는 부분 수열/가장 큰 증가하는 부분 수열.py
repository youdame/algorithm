import sys 
from io import StringIO

input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N

dp[0] = arr[0]
# i로 끝나는 가장 큰 부분 증가 수열

for i in range(N):
    max_value = 0
    max_j = -1
    for j in range(i):
        if arr[i] > arr[j]: # 증가하는 부분 수열 중에 
            max_value = max(dp[j], max_value)
            max_j = j
    dp[i] = max_value + arr[i] 

print(max(dp))