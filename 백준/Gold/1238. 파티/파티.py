import sys
from collections import deque
from io import StringIO
import heapq


input = sys.stdin.readline

N, M, X = map(int, input().split())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    start, end ,T = map(int, input().split())
    adj[start].append((end, T))

answer_arr = [0] * (N+1)
for start in range(1, N+1):
    distances = [1e9] * (N+1)
    heap = []
    # 왜 이거 0이지..
    distances[start] = 0
    heapq.heappush(heap, (0, start))
    
    while heap:
        dist, cur_node = heapq.heappop(heap)

        if dist > distances[cur_node]:
            continue
        
        # 인접한 노드 
        for adj_node, adj_dist in adj[cur_node]:
            # 현재 노드를 거쳐가는 게 더 가깝다면 갱신
            if distances[adj_node] > distances[cur_node] + adj_dist:
                distances[adj_node] = distances[cur_node] + adj_dist
                heapq.heappush(heap, (distances[adj_node], adj_node))
    answer_arr[start] = distances[X]

start = X 
distances = [1e9] * (N+1)
heap = []

distances[start] = 0
heapq.heappush(heap, (0, start))

while heap:
    dist, cur_node = heapq.heappop(heap)

    if dist > distances[cur_node]:
        continue
    
    # 인접한 노드 
    for adj_node, adj_dist in adj[cur_node]:
        # 현재 노드를 거쳐가는 게 더 가깝다면 갱신
        if distances[adj_node] > distances[cur_node] + adj_dist:
            distances[adj_node] = distances[cur_node] + adj_dist
            heapq.heappush(heap, (distances[adj_node], adj_node))
for end in range(1, N+1):
    answer_arr[end] += distances[end]
print(max(answer_arr))
