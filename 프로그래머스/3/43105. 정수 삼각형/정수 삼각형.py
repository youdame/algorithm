def solution(triangle):
    n = len(triangle)
    dp = [[0] * (i+1) for i in range(n)]
    
    
    dp[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(i+1):
            if j == i:
                dp[i][j] = dp[i-1][j-1] 
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) 
            dp[i][j] += triangle[i][j]
    return max(dp[n-1])