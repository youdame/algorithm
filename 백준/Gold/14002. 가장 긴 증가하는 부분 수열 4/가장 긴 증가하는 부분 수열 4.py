import sys 
from io import StringIO


input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N

dp[0] = 1
from_where = [-1] * N
for i in range(N):
    max_value = 0
    max_j = -1
    for j in range(i):
        if arr[i] > arr[j] and dp[j] > max_value: 
            max_value = dp[j]
            max_j = j
    dp[i] = max_value + 1
    # i는 j로부터 왔다
    from_where[i] = max_j
print(max(dp))


want = dp.index(max(dp))


answer = []
while want != -1:
    answer.append(arr[want])
    want = from_where[want]
print(*answer[::-1])