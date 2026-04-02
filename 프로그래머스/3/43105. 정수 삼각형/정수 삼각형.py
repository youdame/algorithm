def solution(triangle):
    n = len(triangle)
    dp = []

    """
    대각선 방향으로 오른쪽 //  대각선 방향으로 왼쪽 가능 

    맨 왼쪽 사람 -> 자기 오른쪽에서 자기로 오는 경우만 있음
    맨 오른쪽 사람 -> 대각선 방향으로 오른쪽만 있음

    아래 사람 기준으로 대각선 방향으로 왼쪽 or 오른쪽에서 오는 거임
    """
    
    for i in range(n):
        dp.append([0] * (i+1)) 
    
    dp[0][0] = triangle[0][0]
    
    # 맨 왼쪽 사람 
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + triangle[i][0]


    # 맨 오른쪽 사람 
    for j in range(1, n):
        dp[j][len(triangle[j])-1] = dp[j-1][len(triangle[j])-1-1] + triangle[j][len(triangle[j])-1] 


    for i in range(1, n):

        for j in range(1, len(triangle[i]) - 1):

            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    

    
    return max(dp[n-1])
