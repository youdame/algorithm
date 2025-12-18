import sys

input = sys.stdin.readline

count = int(input())
str = input().strip()

print(sum([int(i) for i in str]))
