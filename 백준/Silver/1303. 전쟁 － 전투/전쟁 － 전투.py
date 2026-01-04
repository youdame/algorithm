import sys
from io import StringIO
from collections import deque
input = sys.stdin.readline

가로, 세로 = list(map(int, input().split()))

matrix = [list(input().strip()) for i in range(세로)]
visited = [[False] * 가로 for i in range(세로)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = deque([])


def bfs(node, color):
    y, x = node
    visited[y][x] = True
    queue.append((y, x))
    count = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if (
                0 <= ny < 세로
                and 0 <= nx < 가로
                and not visited[ny][nx]
                and matrix[ny][nx] == color
            ):
                visited[ny][nx] = True
                queue.append((ny, nx))
                count += 1
    return count


w_power = 0
b_power = 0
for y in range(세로):
    for x in range(가로):
        if matrix[y][x] == "W" and not visited[y][x]:
            power = bfs((y, x), "W")
            w_power += power * power
        if matrix[y][x] == "B" and not visited[y][x]:
            power = bfs((y, x), "B")
            b_power += power * power
print(w_power, b_power)
