import sys

input = sys.stdin.readline
count = int(input())
arr = [int(input().strip()) for i in range(count)]

empty = []
for element in arr:
    if element == 0:
        empty.pop()
        continue
    empty.append(element)

print(sum(empty))
