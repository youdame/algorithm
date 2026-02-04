import sys 
from io import StringIO
import heapq


input = sys.stdin.readline
N, E = map(int, input().split())

adj = [[] for i in range(N+1)]
for _ in range(E):
    start, end, cost = map(int, input().split())
    adj[start].append((end, cost))
    adj[end].append((start, cost))



A, B = map(int, input().split())

def dijstra(start):
    heap =[]
    distance = [1e9] * (N+1)
    distance[start] = 0
    
    heapq.heappush(heap, (0, start))
    
    while heap:
        dist, node = heapq.heappop(heap) 
        
        if dist > distance[node]:
            continue
        for new_node, cost in adj[node]:
            if distance[new_node] > distance[node] + cost:
                distance[new_node] = distance[node] + cost
                heapq.heappush(heap, (distance[new_node], new_node))
    return distance
dist_from_1 = dijstra(1)
dist_from_A = dijstra(A)
dist_from_B = dijstra(B)

path1 = dist_from_1[A] + dist_from_A[B] + dist_from_B[N]
path2 = dist_from_1[B] + dist_from_B[A] + dist_from_A[N]

answer = min(path1, path2)
print(answer if answer < 1e9 else -1)