import sys
from io import StringIO


input = sys.stdin.readline

n = int(input())
triangle = []

for i in range(n):
    triangle.append(list(map(int, input().split())))


dp = [[triangle[0][0]]]
for i in range(1, len(triangle)):
    arr = []
    for j in range(len(triangle[i])):
        if j == 0:
            arr.append(dp[i-1][0] + triangle[i][j])
        elif j == len(triangle[i]) - 1:
            arr.append(dp[i-1][j-1] + triangle[i][j])
        else:
            arr.append(max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])
    dp.append(arr)
print(max(dp[n-1]))