import sys
from io import StringIO
from collections import deque


input = sys.stdin.readline

N, M = list(map(int, input().split()))

matrix = [list(map(int, input().strip())) for i in range(N)]

count = 1


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue = deque([(0, 0)])
visited = [[False] * M for i in range(N)]
visited[0][0] = True
count = 1
distance = [[-1] * M for i in range(N)]
distance[0][0] = 1


while queue:
    y, x = queue.popleft()
    for dy, dx in directions:
        ny = dy + y
        nx = dx + x

        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and matrix[ny][nx] == 1:
            distance[ny][nx] = distance[y][x] + 1
            visited[ny][nx] = True
            queue.append((ny, nx))
print(distance[N - 1][M - 1])
