import sys 

input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N

dp[0] = 1
# i로 끝나는 가장 긴 부분 감소 수열

for i in range(N):
    max_value = 0
    for j in range(i):
        if arr[i] < arr[j]: # 감소하는 부분 수열 중에 
            max_value = max(dp[j], max_value)
    dp[i] = max_value + 1

print(max(dp))