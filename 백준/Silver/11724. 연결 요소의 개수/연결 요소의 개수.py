import sys
from io import StringIO


input = sys.stdin.readline

N, M = list(map(int, input().split()))
adj = [[] for i in range(N + 1)]
for i in range(M):
    u, v = list(map(int, input().split()))
    adj[u].append(v)
    adj[v].append(u)
visited = [False] * (N + 1)


answer = 0

for index in range(1, len(visited)):
    if visited[index]:
        continue

    answer += 1
    stack = [index]
    visited[index] = True
    while stack:
        node = stack.pop()
        for new_node in adj[node]:
            if not visited[new_node]:
                visited[new_node] = True
                stack.append(new_node)

print(answer)
