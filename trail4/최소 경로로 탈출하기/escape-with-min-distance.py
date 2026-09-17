from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


visited = [[-1] * m for _ in range(n)]

queue = deque([(0, 0)])
visited[0][0] = 0
while queue:
    y, x = queue.popleft()

    for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < n and 0 <= nx < m and a[ny][nx] == 1:
            if visited[ny][nx] == -1 :
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))

print(visited[n-1][m-1])