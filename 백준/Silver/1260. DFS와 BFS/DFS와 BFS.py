import sys
from io import StringIO
from collections import deque


input = sys.stdin.readline

N, M, V = list(map(int, input().split()))
adj = [[] for i in range(N + 1)]
for i in range(M):
    A, B = list(map(int, input().split()))
    adj[A].append(B)
    adj[B].append(A)

# print(adj)


def dfs(start):
    stack = []
    stack.append(start)
    visited = [False] * (N + 1)
    answer = []
    while len(stack) != 0:
        node = stack.pop()
        if visited[node]:
            continue
        answer.append(node)
        visited[node] = True
        for new_node in sorted(adj[node], reverse=True):
            if not visited[new_node]:
                stack.append(new_node)
    print(*answer)


dfs(V)


def bfs(start):
    queue = deque()
    queue.append(start)
    answer = []
    visited = [False] * (N + 1)
    while queue:
        node = queue.popleft()
        if visited[node]:
            continue
        answer.append(node)
        visited[node] = True
        for new_node in sorted(adj[node]):
            if not visited[new_node]:
                queue.append(new_node)

    print(*answer)


bfs(V)
