import sys
from collections import deque
from io import StringIO
import heapq


input = sys.stdin.readline

N, M, X = map(int, input().split())

home_to_party = [[] for _ in range(N+1)]
party_to_home = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, time = map(int, input().split())  
    home_to_party[end].append((start, time))
    party_to_home[start].append((end, time))
"""
자기집 -> X -> 다시 자기집
모든 노드에서 X까지의 거리
X에서 모든 노드까지의 거리 
"""
def dijkstra(start_dist, start_node, adj):
    distance = [1e9] * (N + 1)
    heap = [(start_dist, start_node)]
    distance[start_node] = 0
    
    while heap:
        dist, node = heapq.heappop(heap)

        if dist > distance[node]:
            continue
        for adj_node, adj_dist in adj[node]:
            if distance[adj_node] > distance[node] + adj_dist:
                distance[adj_node] = distance[node] + adj_dist
                heapq.heappush(heap, (distance[adj_node], adj_node))
    return distance[1:]    

h_to_p_distance = dijkstra(0, X, home_to_party)
p_to_h_distance = dijkstra(0, X, party_to_home)

total_distance = []
for i in range(N):
    total_distance.append(h_to_p_distance[i] + p_to_h_distance[i])
print(max(total_distance))
