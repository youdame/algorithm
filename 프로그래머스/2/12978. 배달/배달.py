from collections import defaultdict, deque

def solution(N, road, K):

    adj = defaultdict(list)
    for a, b , c in road:
        
        adj[a].append((b, c))
        
        adj[b].append((a, c))
    
    queue = deque([(1, 0)])
    
    
    visited = [float("inf")] *(N+1)
    visited[1] = 0
    while queue:
        node, time = queue.popleft()
        # if time > visited[node]:
        #     continue
        for new_node, w in adj[node]:
            if time + w < visited[new_node]:
                visited[new_node] = time + w
                queue.append((new_node, time + w))

    answer= 0
    
    for dist in visited[1:]:
        if dist <= K:
            answer +=1
    return answer
                
        
        