import sys
from io import StringIO
from collections import deque


input = sys.stdin.readline

n, m = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for i in range(n)]

visited = [[False] * m for i in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(node):
    queue = deque([node])

    visited[node[0]][node[1]] = True
    너비 = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if (
                0 <= ny < n
                and 0 <= nx < m
                and not visited[ny][nx]
                and matrix[ny][nx] == 1
            ):
                visited[ny][nx] = True
                queue.append((ny, nx))
                너비 += 1
    return 너비


count = 0
max_넓이 = 0
for y in range(n):
    for x in range(m):
        if not visited[y][x] and matrix[y][x] == 1:
            현넓이 = bfs((y, x))
            if max_넓이 < 현넓이:
                max_넓이 = 현넓이

            count += 1
print(count)
print(max_넓이)
