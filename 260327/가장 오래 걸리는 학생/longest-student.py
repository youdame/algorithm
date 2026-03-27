import heapq
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 최단 거리 구하기 

"""
다익스트라 알고리즘 
최단 거리 구하는 문제 
그냥 bfs 돌면서 거리 갱신해주면 되는 거 아님?


1에서 n번까지 가보기 ~~~~
2에서 n번까지 
3에서 n번까지
"""

adj = [[] for _ in range(n+1)]


for i, j, d in edges:
    adj[j].append((i, d))
    adj[i].append((j, d))

school = n

answer = 0
for start in range(1, n):
    distances = [1e9] * (n + 1) 
    distances[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        dist, node = heapq.heappop(heap)

        if dist > distances[node]:
            continue

        for adj_node, adj_dist in adj[node]:
            # 현재 node를 거쳐서 가는 게 좋은지? -> 
            if distances[adj_node] > distances[node] + adj_dist:
                distances[adj_node] = distances[node] + adj_dist
                heapq.heappush(heap, (distances[adj_node], adj_node,))
    answer = max(distances[n] , answer)

print(answer)
