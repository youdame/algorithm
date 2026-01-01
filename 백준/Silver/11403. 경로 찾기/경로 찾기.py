import sys
from io import StringIO
from collections import deque

input = sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().split(" "))) for i in range(N)]
adj = [[] for i in range(N)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            adj[i].append(j)
answer = [[0] * N for i in range(N)]


def bfs(node):
    visited = [False] * N
    queue = deque([node])
    answer = [0] * N
    while queue:
        pop_node = queue.popleft()

        for new_node in adj[pop_node]:
            if not visited[new_node]:
                visited[new_node] = True
                queue.append(new_node)
                answer[new_node] = 1

    return answer


for i in range(N):
    print(*bfs(i))
