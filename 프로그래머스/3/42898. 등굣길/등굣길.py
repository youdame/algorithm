def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    print(dp)
    
    
    for i in range(len(puddles)):
        j, k = puddles[i]
        puddles[i] = [k-1, j-1]
        
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if [i, j] in puddles or (i, j) == (0, 0):
                continue
            
            if i == 0:
                dp[i][j] = (dp[i][j-1]) % 1000000007
            elif j == 0:
                dp[i][j] = (dp[i-1][j]) % 1000000007
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1] ) % 1000000007

    return dp[-1][-1]
            