import sys
from io import StringIO
from collections import deque

input = sys.stdin.readline

N, M = list(map(int, input().split()))
adj = [[] for i in range(N + 1)]

answer = []
for i in range(M):
    u, v = list(map(int, input().split()))
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, N + 1):

    visited = [False] * (N + 1)
    거리 = [-1] * (N + 1)
    queue = deque()
    queue.append(i)
    거리[i] = 0

    while queue:
        node = queue.popleft()
        visited[node] = True

        for new_node in adj[node]:
            if not visited[new_node]:
                visited[new_node] = True
                queue.append(new_node)
                if 거리[new_node] == -1:
                    거리[new_node] = 거리[node] + 1
    answer.append(sum(거리[1:]))
print(answer.index(min(answer)) + 1)
