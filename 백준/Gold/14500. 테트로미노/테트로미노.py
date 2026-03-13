import sys
from io import StringIO

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    
visited = [[False] * M for x in range(N)]

max_sum = -1e9   

def dfs(y, x, depth, total):
    global max_sum
    if depth == 4:
        max_sum = max(max_sum, total)
        return  
    for direction in directions:
            dy, dx = direction
            ny = dy + y
            nx = dx + x
            
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    dfs(ny, nx, depth+1, total+ arr[ny][nx])
                    visited[ny][nx] = False
  

for y in range(N):
    for x in range(M):
        visited[y][x] = True
        dfs(y, x, 1, arr[y][x])
        visited[y][x] = False
              


    
                    
                 
for y in range(N):
    for x in range(M):
        vals = []
        for direction in directions:
            dy, dx = direction
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < M:
                vals.append(arr[ny][nx])
        if len(vals) >= 3:
            total = arr[y][x] + sum(sorted(vals, reverse = True)[:3])
            max_sum = max(max_sum, total)

print(max_sum)





