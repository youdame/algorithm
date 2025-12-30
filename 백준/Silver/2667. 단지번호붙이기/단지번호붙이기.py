import sys
from io import StringIO


input = sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().strip())) for i in range(N)]
visited = [[False] * N for i in range(N)]
# print(matrix)
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def dfs(node):
    node_count = 1
    stack = [node]
    visited[node[0]][node[1]] = True
    while stack:
        y, x = stack.pop()
        for dy, dx in directions:
            ny = dy + y
            nx = dx + x
            if (
                0 <= nx < N
                and 0 <= ny < N
                and not visited[ny][nx]
                and matrix[ny][nx] == 1
            ):
                visited[ny][nx] = True
                stack.append((ny, nx))
                node_count += 1
    return node_count


count = 0
answer = []
for y in range(N):
    for x in range(N):
        if not visited[y][x] and matrix[y][x] == 1:
            answer.append(dfs((y, x)))
            count = count + 1

print(count)
for element in sorted(answer):
    print(element)
