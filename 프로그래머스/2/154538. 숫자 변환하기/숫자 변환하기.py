from collections import deque 

def solution(x, y, n):
    
    answer = 1e9
    queue = deque([(x, 0)])
    visited = set()
    visited.add(x)
    
    def bfs(start, count):
        while queue:
            node, count = queue.popleft()
            if node == y:
                return count
            for  next_node in (node + n , node *2, node * 3):
                if next_node <= y and next_node not in visited:
                    visited.add(next_node)
                    queue.append((next_node , count + 1))
        return -1
    
    return bfs(x, 0)
