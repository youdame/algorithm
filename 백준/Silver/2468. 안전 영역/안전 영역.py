import sys 
from io import StringIO
from collections import deque


input = sys.stdin.readline 
N = int(input())

arr= []
max_height = -1e9
for _ in range(N):
    element = list(map(int, input().split()))
    arr.append(element)
    max_height = max(max_height, max(element))
    
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


max_count = -1e9
for water_height in range(0, max_height):
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
           if arr[i][j] <= water_height:
               temp[i][j] = 0
           else:
               temp[i][j] = 1

    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if temp[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                queue = deque([(i, j)])
    
                while queue:
                    y, x = queue.popleft()
                    for direction in directions:
                        dy, dx = direction
                        ny = dy + y
                        nx = dx + x
                        if 0 <= ny < N and 0 <= nx < N:
                            if not visited[ny][nx] and temp[ny][nx] == 1:
                                queue.append((ny, nx))
                                visited[ny][nx] = True
                count += 1
    max_count = max(max_count, count)
print(max_count)