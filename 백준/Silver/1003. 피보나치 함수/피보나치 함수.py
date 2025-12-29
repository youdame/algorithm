import sys
from io import StringIO

input = sys.stdin.readline

T = int(input())

arr = [int(input()) for i in range(T)]


영 = [0] * (41)
일 = [0] * (41)

dp = [-1] * (41)
dp[0] = 0
dp[1] = 1

영[0] = 1
영[1] = 0
일[0] = 0
일[1] = 1

for i in range(2, 41):
    dp[i] = dp[i - 1] + dp[i - 2]
    영[i] = 영[i - 1] + 영[i - 2]
    일[i] = 일[i - 1] + 일[i - 2]

for element in arr:
    print(영[element], 일[element])
