import sys
from io import StringIO
from collections import deque

input = sys.stdin.readline
N, M = list(map(int, input().split()))
matrix = [list(map(int, input().strip().split(" "))) for i in range(N)]
distance = [[-1] * M for i in range(N)]
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

visited = [[False] * M for i in range(N)]


def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node[0]][node[1]] = True
    distance[node[0]][node[1]] = 0
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny = dy + y
            nx = dx + x
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                if matrix[ny][nx] == 1:
                    visited[ny][nx] = True
                    distance[ny][nx] = distance[y][x] + 1
                    queue.append((ny, nx))


for y in range(N):
    for x in range(M):
        if matrix[y][x] == 0:
            distance[y][x] = 0

        if matrix[y][x] == 2:
            bfs((y, x))
for element in distance:
    print(*element)
