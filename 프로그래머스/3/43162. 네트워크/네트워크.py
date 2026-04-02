from collections import deque
    
def solution(n, computers):
    
    visited = [False] * n
    
    def bfs(node, visited):
        visited[node] = True
        queue = deque([node])

        
        while queue:

            cur_node = queue.popleft()
            
            cur_adj_arr = computers[cur_node]
            
            for new_node in range(n):
                is_adj = cur_adj_arr[new_node]

                if new_node != cur_node and not visited[new_node] :
                    if is_adj == 1:
                        queue.append(new_node)
                        visited[new_node] = True


    
    count = 0
    
    for i in range(n):
        if not visited[i]:
            is_new = bfs(i, visited)            
            count += 1
    return count