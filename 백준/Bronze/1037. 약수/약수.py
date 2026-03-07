import sys

input = sys.stdin.readline

n = int(input())
divisors = list(map(int, input().split()))

print(min(divisors) * max(divisors))