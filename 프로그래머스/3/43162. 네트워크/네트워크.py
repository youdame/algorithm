from collections import deque

def solution(n, computers):
    visited = [False] * n
    
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            queue = deque([i])
            visited[i] = True
            
            while queue :
                node = queue.popleft()
                for j in range(n):
                    if not visited[j] and node != j and computers[node][j] == 1:
                        visited[j] = True
                        queue.append(j)
    return answer    
            
                    
        
                