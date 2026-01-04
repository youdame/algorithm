import sys
from io import StringIO
from collections import deque


input = sys.stdin.readline

n, m = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for i in range(n)]

visited = [[False] * m for i in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
queue = deque([])

distance = [[-1] * m for i in range(n)]


def bfs():
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))
                distance[ny][nx] = distance[y][x] + 1


for y in range(n):
    for x in range(m):
        if matrix[y][x] == 1:
            visited[y][x] = True
            distance[y][x] = 0
            queue.append((y, x))
bfs()
print(max([x for row in distance for x in row]))
