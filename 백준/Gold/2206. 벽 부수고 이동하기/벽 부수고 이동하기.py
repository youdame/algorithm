import sys
from collections import deque
from io import StringIO


input = sys.stdin.readline

arr = []

N, M = map(int, input().split())
for _ in range(N):
    arr.append(list(map(int, input().strip())))


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs():
    # visited_distance[i][j][broken] = broken 여부에 따른 i,j까지 가는 거리
    
    visited_distance = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited_distance[0][0][0] = 1
    queue = deque([(0, 0, 0)])

    while queue:
        y, x, broken = queue.popleft()
        if y == N - 1 and x == M - 1:
            return visited_distance[y][x][broken]

        for dy, dx in directions:
            ny, nx = dy + y, dx + x

            # 경로 안에 있고 
            if 0 <= ny < N and 0 <= nx < M:
                # 지금 벽이야 근데 아직 안 부셨어! 부실 수 있어!
                if arr[ny][nx] == 1 and broken == 0:
                    if visited_distance[ny][nx][broken] == 0:
                        # 부시자
                        visited_distance[ny][nx][1] = visited_distance[y][x][0] + 1
                        queue.append((ny, nx, 1))

                # 지금 벽이 아니야 => 현상유지
                elif arr[ny][nx] == 0:
                    if visited_distance[ny][nx][broken] == 0:
                        visited_distance[ny][nx][broken] = visited_distance[y][x][broken] + 1
                        queue.append((ny, nx, broken))
    return -1


print(bfs())