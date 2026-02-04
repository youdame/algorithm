import sys 
from io import StringIO
import heapq

input = sys.stdin.readline
N = int(input())
M = int(input())
adj = [[] for i in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    adj[start].append((end, cost))


heap =[]
A, B = map(int, input().split())

distance = [1e9] * (N+1)
prev = [-1] * (N+1)
distance[A] = 0

heapq.heappush(heap, (0, A))

while heap:
    dist, node = heapq.heappop(heap) 
    
    if dist > distance[node]:
        continue
    for new_node, cost in adj[node]:
        if distance[new_node] > distance[node] + cost:
            distance[new_node] = distance[node] + cost
            heapq.heappush(heap, (distance[new_node], new_node))
            prev[new_node] = node


path = []
cur = B

while cur != -1:
    path.append(cur)
    cur = prev[cur]

path.reverse()
print(distance[B])
print(len(path))
print(*path)
    
        
    