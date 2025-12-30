import sys
from io import StringIO

input = sys.stdin.readline

N, M = list(map(int, input().split()))

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

matrix = [list(input().strip()) for i in range(N)]

for y in range(N):
    for x in range(M):
        if matrix[y][x] == "I":
            start = (y, x)

stack = [start]
visited = [[False] * M for i in range(N)]
visited[start[0]][start[1]] = True
count = 0
while stack:
    node = stack.pop()
    # print(stack)

    if matrix[node[0]][node[1]] == "P":
        count += 1
    for dy, dx in directions:
        ny = node[0] + dy
        nx = node[1] + dx
        if 0 <= ny < N and 0 <= nx < M:
            if not visited[ny][nx] and matrix[ny][nx] != "X":
                visited[ny][nx] = True
                stack.append((ny, nx))
print(count if count > 0 else "TT")
