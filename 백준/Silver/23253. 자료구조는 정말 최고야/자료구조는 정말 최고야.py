import sys
from io import StringIO

input = sys.stdin.readline


N, 더미수 = list(map(int, input().split()))

stacks = []
book_to_stack = {}
for i in range(더미수):
    교과서수 = int(input())
    stack = list(map(int, input().split()))

    stacks.append(stack)
    for book in stack:
        book_to_stack[book] = i
책번호 = 1

found = True
while 책번호 <= N:

    if stacks[book_to_stack[책번호]][-1] == 책번호:
        stacks[book_to_stack[책번호]].pop()
        책번호 += 1
    else:
        found = False
        break
print("Yes" if found else "No")
