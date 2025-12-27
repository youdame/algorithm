import sys
from io import StringIO


input = sys.stdin.readline

N = int(input())
answer = [-1] * (N + 1)

adj = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
for i in range(N - 1):
    v, w = list(map(int, input().split()))
    adj[v].append(w)
    adj[w].append(v)

visited[1] = True
stack = [1]
while stack:
    node = stack.pop()
    for new_node in adj[node]:
        if not visited[new_node]:
            stack.append(new_node)
            visited[new_node] = True
            answer[new_node] = node
print("\n".join(map(str, answer[2:])))
