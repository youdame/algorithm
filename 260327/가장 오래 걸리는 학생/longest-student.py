n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 최단 거리 구하기 

"""
다익스트라 알고리즘 
최단 거리 구하는 문제 
그냥 bfs 돌면서 거리 갱신해주면 되는 거 아님?
"""

adj = {}

distance = [[1e9] * n for _ in range(n)]
for i, j, d in edges:
    if j not in adj or i not in adj:
        adj[j] = [(i, d)]
        adj[i] = [(j, d)]
    else:
        adj[j].append((i, d))
        adj[i].append((j, d))
print(adj)
school = n
