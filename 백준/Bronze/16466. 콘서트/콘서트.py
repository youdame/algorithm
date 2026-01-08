import sys
from io import StringIO


input = sys.stdin.readline


N = int(input())
tickets = sorted(list(map(int, input().split())))


min_value = 1
for ticket in tickets:
    if min_value == ticket:
        min_value += 1


print(min_value)
