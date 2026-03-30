import sys
from io import StringIO
from collections import deque



input = sys.stdin.readline


N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().strip())))

visited = [[False] * N for _ in range(N)]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def bfs(node):
    count = 1
    i, j = node 
    queue = deque([(i, j)])
    visited[i][j] = True


    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny , nx = dy+ y , dx + x

            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx] and arr[ny][nx] == 1:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                    count += 1
    return count 

단지_count = 0
마을_count_arr = []    
for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] == 1:
            마을_count = bfs((i, j))
            마을_count_arr.append(마을_count)
            단지_count += 1
            
print(단지_count)
for element in sorted(마을_count_arr):
    print(element)