def solution(land):
    
    n = len(land)
    m = len(land[0])
    
    
    dp = [[0] * m for _ in range(n)]
    
    for j in range(m):
        dp[0][j] = land[0][j]
        
    
    for i in range(1, n):
        for j in range(m):
        
            dp[i][j] = max(dp[i-1][0:j] + dp[i-1][j+1:]) + land[i][j]
            
    return max(dp[n-1])