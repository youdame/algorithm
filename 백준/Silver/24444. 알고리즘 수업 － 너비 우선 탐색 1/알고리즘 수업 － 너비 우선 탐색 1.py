import sys 
from io import StringIO
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())

adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)    
    adj[v].append(u)


queue = deque([])
queue.append(R)
visited[R] = True

경로 = [0] * (N+1)
경로[R] = 1
order = 2

while queue:
    node = queue.popleft()
    for new_node in sorted(adj[node]):
        if not visited[new_node]:
            queue.append(new_node)
            visited[new_node] = True
            경로[new_node] = order
            order += 1
            
for element in 경로[1:]:
    print(element)
    