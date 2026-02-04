import sys 
from io import StringIO

input = sys.stdin.readline

N = int(input())

a, b ,c = (list(map(int, input().split())))
max_prev_dp = [a, b, c]
min_prev_dp = [a, b, c]

for i in range(1, N):
        a, b ,c = (list(map(int, input().split())))
        
        max_curr_dp = [max(max_prev_dp[0], max_prev_dp[1]) + a, max(max_prev_dp[0], max_prev_dp[1], max_prev_dp[2]) + b,
                       max(max_prev_dp[1], max_prev_dp[2]) + c]

        min_curr_dp = [min(min_prev_dp[0], min_prev_dp[1]) + a, min(min_prev_dp[0], min_prev_dp[1], min_prev_dp[2]) + b,
                       min(min_prev_dp[1], min_prev_dp[2]) + c]
        max_prev_dp = max_curr_dp
        min_prev_dp = min_curr_dp
    
print(max(max_prev_dp),min(min_prev_dp))
