from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    distance = [[-1] * m for i in range(n)]
    visited = [[False] * m for i in range(n)]
    queue = deque([(0, 0)])
    distance[0][0] = 1
    visited[0][0] = True
    
    while queue:
        y, x = queue.popleft()
        
        for dy, dx in directions:
            ny = dy + y
            nx = dx + x
            
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and maps[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                    distance[ny][nx] = distance[y][x] + 1
                
    if distance[n-1][m-1] == -1:
        return -1 
    else: 
        return distance[n-1][m-1]

        