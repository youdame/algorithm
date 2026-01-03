import sys
from io import StringIO
from collections import deque



input = sys.stdin.readline


N = int(input())
adj = [[] for i in range(N + 1)]
M = int(input())
for i in range(N):
    요소들 = list(map(int, input().strip().split()))
    for j in range(N):
        if 요소들[j] == 1:
            if j + 1 not in adj[i + 1]:
                adj[i + 1].append(j + 1)
            if i + 1 not in adj[j + 1]:
                adj[j + 1].append(i + 1)
route = list(map(int, input().strip().split()))

# print(adj)

visited = [False] * (N + 1)


def bfs(node):
    queue = deque([])
    queue.append(node)
    visited[node] = True
    node_route = [node]

    while queue:
        pop_node = queue.popleft()
        for new_node in adj[pop_node]:
            # print(new_node)
            if not visited[new_node]:
                visited[new_node] = True
                queue.append(new_node)
                node_route.append(new_node)
    return node_route


flag = True


시작 = bfs(route[0])
for node in route:
    if node not in 시작:
        flag = False
        break

print("YES" if flag else "NO")
