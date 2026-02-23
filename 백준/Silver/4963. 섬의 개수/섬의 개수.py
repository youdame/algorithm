import sys
from io import StringIO
from collections import deque 



directions = [(0, 1), (-1, 0), (1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

while True:    
    W, H = map(int, input().split())
    if W == H == 0:
        break
    arr = []
    for _ in range(H):
        arr.append(list(map(int, input().split())))
    visited = [[False] * W for _ in range(H)]

    answer = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 1 and not visited[i][j]:
                queue = deque([])
                queue.append((i, j))
                visited[i][j] = True
                answer += 1
                while queue:
                    y, x = queue.popleft()
                    for direction in directions:
                        dy, dx = direction
                        nx = dx + x
                        ny = dy + y
                        if 0 <= nx < W and 0 <= ny < H and not visited[ny][nx]:
                            if arr[ny][nx] == 1:
                                queue.append((ny, nx))
                                visited[ny][nx] = True
    print(answer)
        
    
    

    