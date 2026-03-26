import sys 
from io import StringIO



input = sys.stdin.readline
"""
2×n 직사각형을 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

3
171
2731
845100400152152934331135470251
1071292029505993517027974728227441735014801995855195223534251
"""


while True:
    try:
        N = int(input())
    
        dp = [0 for _ in range(max(N + 1, 4))]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 3
        
        for i in range(3, N + 1):
            dp[i] = (dp[i-1] + dp[i-2] * 2)
        print(dp[N])
    except:
        break
    