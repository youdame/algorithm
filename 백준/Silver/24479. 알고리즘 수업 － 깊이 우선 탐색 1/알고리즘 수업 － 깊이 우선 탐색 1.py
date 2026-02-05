import sys 
from io import StringIO

input = sys.stdin.readline

N, M, R = map(int, input().split())

adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)    
    adj[v].append(u)


stack = []
stack.append(R)


경로 = [0] * (N+1)
order = 1
while stack:
    node = stack.pop()
    if visited[node]:
        continue
    visited[node] = True
    경로[node] = order
    order += 1
    
    for new_node in sorted(adj[node],reverse=True):
        if not visited[new_node]:
            stack.append(new_node)
            
for element in 경로[1:]:
    print(element)
    