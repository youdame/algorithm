import sys 
from io import StringIO

input = sys.stdin.readline

k = int(input())

arr = list(input().strip().replace(" ", ""))


answer = []

min_value = None
max_value = None

def dfs(depth):
    global min_value, max_value

    if depth == k + 1:
        value = "".join(map(str, answer))
        if min_value is None:
            min_value = value
        max_value = value
        return

    for digit in range(10):
        if digit in answer:
            continue

        if depth > 0:
            if arr[depth - 1] == "<" and answer[-1] > digit:
                continue
            if arr[depth - 1] == ">" and answer[-1] < digit:
                continue

        answer.append(digit)
        dfs(depth + 1)
        answer.pop()
dfs(0)

print(max_value)
print(min_value)
