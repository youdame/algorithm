from collections import deque
def solution(n, computers):
    
    visited = [False] * n
    
    count = 0
    
    for i in range(len(computers)):
        if not visited[i]:
            count += 1
            queue = deque([i])
            visited[i] = True
            
            while queue:
                node = queue.popleft()
                
                adj = computers[node]
                for j in range(len(computers[node])):
                    if j != i and adj[j] == 1 and not visited[j]:
                        queue.append(j)
                        visited[j] = True

    return count
            