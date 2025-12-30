import sys
from io import StringIO


input = sys.stdin.readline

N = int(input())

matrix = [list(input().strip()) for i in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[False] * N for i in range(N)]


real_answer = 0


def dfs(start, color):
    answer = 0
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()

        if not visited[node[0]][node[1]]:
            answer += 1
        for dy, dx in directions:
            ny = node[0] + dy
            nx = node[1] + dx
            if (
                0 <= nx < N
                and 0 <= ny < N
                and not visited[ny][nx]
                and matrix[ny][nx] in color
            ):
                visited[ny][nx] = True
                stack.append((ny, nx))
    return answer


for i in range(N):
    for j in range(N):
        if matrix[i][j] == "R":
            real_answer += dfs((i, j), ["R"])
        elif matrix[i][j] == "G":
            real_answer += dfs((i, j), ["G"])
        elif matrix[i][j] == "B":
            real_answer += dfs((i, j), ["B"])
print(real_answer)
visited = [[False] * N for i in range(N)]
real_answer = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == "R" or matrix[i][j] == "G":
            real_answer += dfs((i, j), ["R", "G"])

        elif matrix[i][j] == "B":
            real_answer += dfs((i, j), ["B"])
print(real_answer)
