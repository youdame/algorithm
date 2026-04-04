import sys
from collections import deque
from io import StringIO


input = sys.stdin.readline


arr = []

N, M = map(int, input().split())
for _ in range(N):
    arr.append(list(map(int, input().strip())))

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

wall_locations = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            wall_locations.append((i, j))


visited = [[[0] * 2 for _ in range(M)]  for _ in range(N)]
distances = [[[0] * 2 for _ in range(M)] for _ in range(N)]

def bfs():
    visited[0][0][0] = True
    distances[0][0][0] = 1

    # 좌표 + 깨짐 여부 
    queue = deque([(0, 0, 0)])
    
    while queue:
        y, x, broken = queue.popleft()

        # 목적지 도달 시 해당 상태의 거리를 반환
        if y == N - 1 and x == M - 1:
            return distances[y][x][broken]
            
        for dy, dx in directions:
            ny, nx = dy + y, dx + x

            if 0 <= ny < N and 0 <= nx < M :
                if arr[ny][nx] == 0 and not visited[ny][nx][broken] :
                    visited[ny][nx][broken] = True
                    distances[ny][nx][broken] = distances[y][x][broken] + 1
                    queue.append((ny,nx, broken))
                    
                elif arr[ny][nx] == 1 and not broken and not visited[ny][nx][1]:
                    visited[ny][nx][1] = True
                    distances[ny][nx][1] = distances[y][x][0] + 1
                    queue.append((ny,nx, 1))
    return -1
print(bfs())
