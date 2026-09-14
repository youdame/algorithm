from collections import deque, defaultdict
def solution(n, wires):
    answer = 1e9
    wires = deque(wires)
    for i in range(n-1):
        pop_wire = wires.popleft()
        
        visited = [False] * (n + 1)
        record = defaultdict(list)
        
        
        for a, b in wires:
            record[a].append(b)
            record[b].append(a)
    
        for k in range(1, n+1):
            size = 0
            if not visited[k]:
                
                
                queue = deque([k])
                visited[k] = True
                while queue:
                    node = queue.popleft()
                    size += 1
                    
                    for next_node in record[node]:
                        if not visited[next_node]:
                            visited[next_node] = True
                            queue.append(next_node)

            diff = abs(size - (n - size))
            answer = min(answer, diff)
        
        
        wires.append(pop_wire)
        
    return answer