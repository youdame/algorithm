N = int(input())

# Please write your code here.


dp = []
for i in range(N):
    if i == 0 or i == 1:
        dp.append(1)
        continue
    dp.append(dp[i-1] + dp[i-2])

print(dp[N-1])