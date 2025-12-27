import sys
from io import StringIO

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

N, M = list(map(int, input().split()))
adj = [[] for i in range(N + 1)]
for i in range(M):
    u, v = list(map(int, input().split()))
    adj[u].append(v)
    adj[v].append(u)
visited = [False] * (N + 1)


def bfs(node):
    visited[node] = True
    for new_node in adj[node]:
        if not visited[new_node]:
            visited[new_node] = True
            bfs(new_node)


answer = 0

for index in range(1, len(visited)):
    if visited[index]:
        continue
    else:
        answer += 1
        bfs(index)

print(answer)
