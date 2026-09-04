from collections import defaultdict, deque

def solution(n, edge):
    adj = defaultdict(list)
    
    
    for start, end in edge:
        adj[start].append(end)
        adj[end].append(start)
    # print(adj)
    
    
    distance = [float('inf')] * (n + 1)
    distance[1] = 0
    queue = deque([1])
    
    while queue:
        node = queue.popleft()
        
        for next_node in adj[node]:
            if distance[next_node] == float("inf"):
                queue.append(next_node)
                distance[next_node] = distance[node] + 1
    max_dist = max(distance[1:])

    return distance.count(max_dist)