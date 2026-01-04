import sys
from io import StringIO
from collections import deque

input = sys.stdin.readline

M, N = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for i in range(N)]


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


distance = [[-1] * M for i in range(N)]

visited = [[False] * M for i in range(N)]

queue = deque([])


def bfs():
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny = dy + y
            nx = dx + x
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx] and matrix[ny][nx] == 0:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                    if distance[ny][nx] != -1 and distance[ny][nx] < distance[y][x] + 1:
                        distance[ny][nx] = distance[ny][nx]
                    else:
                        distance[ny][nx] = distance[y][x] + 1


for y in range(N):
    for x in range(M):
        if matrix[y][x] == 1:
            visited[y][x] = 1
            distance[y][x] = 0
            queue.append((y, x))

        if matrix[y][x] == -1:
            distance[y][x] = 0
bfs()

flat_distance = [x for row in distance for x in row]
if -1 in flat_distance:
    print(-1)
else:
    print(max(flat_distance))
