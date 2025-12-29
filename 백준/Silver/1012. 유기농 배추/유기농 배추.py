import sys
from io import StringIO


input = sys.stdin.readline

T = int(input())

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def dfs():
    while stack:
        node = stack.pop()

        visited[node[0]][node[1]] = True
        for dy, dx in directions:
            ny = dy + node[0]
            nx = dx + node[1]
            if ny >= 0 and ny < N and nx >= 0 and nx < M:
                if not visited[ny][nx] and matrix[ny][nx] == 1:
                    stack.append((ny, nx))


for i in range(T):
    M, N, K = list(map(int, input().split()))
    matrix = [[0] * M for i in range(N)]
    stack = []
    for j in range(K):
        X, Y = list(map(int, input().split()))
        matrix[Y][X] = 1

    visited = [[False] * M for i in range(N)]
    count = 0
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1 and not visited[y][x]:
                count += 1
                stack.append((y, x))
                dfs()
    print(count)
