from collections import deque
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    visited = [[False] * M for _ in range(N)]
    distance = [[1e9] * M for _ in range(N)]
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    visited[0][0] = True
    distance[0][0] = 1
    queue = deque([(0,0)])
    
    while queue:
        y, x = queue.popleft()
        
        for dy, dx in directions:
            ny = dy+ y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if maps[ny][nx] == 1:
                    visited[ny][nx] = True
                    distance[ny][nx] = distance[y][x] + 1
                    queue.append((ny, nx))
                    
    return distance[N-1][M-1] if distance[N-1][M-1] != 1e9 else -1