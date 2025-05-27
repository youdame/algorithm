import sys

input = sys.stdin.readline

n = input()
print(list(map(int, input().strip().split(" "))).count(int(input())))
