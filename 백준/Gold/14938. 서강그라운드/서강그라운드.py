import sys 
from io import StringIO
import heapq


input = sys.stdin.readline


n, m, r = (list(map(int, input().split())))

item_count = (list(map(int, input().split())))

adj = [[] for i in range(n+1)] 

for _ in range(r):
    a, b, l = (list(map(int, input().split())))
    adj[a].append((b, l))
    adj[b].append((a, l))


def dijkstra(start):
    distance = [1e9] * (n+1)
    distance[start] = 0   
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distance[node]:
            continue

        for adj_node, length in adj[node]:
            if distance[node] + length < distance[adj_node]:
                distance[adj_node] = distance[node] + length
                heapq.heappush(heap, (distance[adj_node], adj_node))
    return (distance)
max_count = 0 
for node in list(range(1, n)):
    count = 0
    distance = dijkstra(node)
    
    for index in range(1, len(distance)):
        if distance[index] <= m:
            count += item_count[index - 1]
    max_count = max(count, max_count)
print(max_count)
