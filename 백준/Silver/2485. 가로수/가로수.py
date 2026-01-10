import sys
from io import StringIO

input = sys.stdin.readline
N = int(input())


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


arr = [int(input()) for i in range(N)]
gap_arr = []
for i in range(1, N):
    gap_arr.append(arr[i] - arr[i - 1])

최대공약수 = gcd(gap_arr[0], gap_arr[1])
for i in range(2, len(gap_arr)):
    최대공약수 = gcd(최대공약수, gap_arr[i])


answer = 0
for i in range(len(arr) - 1):
    if arr[i] + 최대공약수 != arr[i + 1]:
        answer += (arr[i + 1] - arr[i]) // 최대공약수 - 1
print(answer)
