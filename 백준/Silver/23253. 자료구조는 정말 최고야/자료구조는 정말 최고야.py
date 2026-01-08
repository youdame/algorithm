import sys
from io import StringIO


input = sys.stdin.readline


N, 더미수 = list(map(int, input().split()))

stacks = []
book_to_stack = {}

possible = True
for i in range(더미수):
    교과서수 = int(input())
    stack = list(map(int, input().split()))

    정렬여부 = stack == sorted(stack, reverse=True)
    if not 정렬여부:
        possible = False
        break

print("Yes" if possible else "No")
