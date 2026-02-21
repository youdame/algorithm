import sys
from io import StringIO
from collections import deque

T = int(input())


directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

for _ in range(T):
    N = int(input())
    queue = deque([])
    y1, x1 = map(int , input().split())
    
    distance = [[1e9] * N for _ in range(N)]
    visited = [[False] * N  for _ in range(N)]

    queue.append((y1,x1))
    distance[y1][x1] = 0
    visited[y1][x1] = True


    y2, x2 = map(int , input().split())
    while queue:
        y, x = queue.popleft()            
        for direction in directions:
            dy, dx = direction 
            nx = dx + x
            ny = dy + y
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                visited[ny][nx] = True
                distance[ny][nx] = min(distance[ny][nx] , distance[y][x] + 1)
                queue.append((ny, nx))
        if y == y2 and x == x2:
            break
    print(distance[y2][x2])