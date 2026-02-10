import sys 
from io import StringIO
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([])
queue.append(N)

distance = [1e9] * 100001
visited = [False] * 100001
distance[N] = 0
visited[N] = True
while queue:
    node = queue.popleft()
    x1 = node + 1
    x2 = node - 1
    x3 = node * 2
    for next in [x1, x2, x3]:
        if 0 <= next <= 100000 and not visited[next]:
            visited[next] = True
            queue.append(next)
            distance[next] = min(distance[next], distance[node] + 1)
    
print(distance[K])