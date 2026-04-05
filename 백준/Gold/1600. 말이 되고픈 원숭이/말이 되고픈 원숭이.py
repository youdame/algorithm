import sys
from collections import deque
from io import StringIO


input = sys.stdin.readline


K = int(input())
arr = []

W, H = map(int, input().split())
for _ in range(H):
    arr.append(list(map(int, input().split())))

# K번 이외의 인접 칸 
other_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
K_directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

def bfs():
    visited = [[[-1] * (K+1)  for _ in range(W)] for _ in range(H)]
    queue = deque([(0, 0, 0)]) # y, x, horse_count
    visited[0][0][0] = 0
    
    while queue:
        y, x, horse_count = queue.popleft()

        if y == H - 1 and x == W - 1:
            return visited[y][x][horse_count]

        # 안되는 경우를 제외하고 둘 다 경우를 따져야함
        # 말의 이동으로 가는 경우 
        if horse_count < K:
            for dy, dx in K_directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < H and 0 <= nx < W:
                    if visited[ny][nx][horse_count+1] == -1:
                        if arr[ny][nx] == 0:
                            queue.append((ny, nx, horse_count + 1))
                            visited[ny][nx][horse_count+1] = visited[y][x][horse_count] + 1

        # 그냥 이동하는 경우  
        for dy, dx in other_directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < H and 0 <= nx < W:
                    if visited[ny][nx][horse_count] == -1:
                        if arr[ny][nx] == 0:
                            queue.append((ny, nx, horse_count))
                            visited[ny][nx][horse_count] = visited[y][x][horse_count] + 1
    
    
    return -1
print(bfs())