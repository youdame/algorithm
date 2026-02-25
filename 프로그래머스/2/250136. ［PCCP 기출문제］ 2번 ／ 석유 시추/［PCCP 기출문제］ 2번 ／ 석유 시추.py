from collections import deque, defaultdict
   
def solution(land):
    n = len(land)
    m = len(land[0])
    queue = deque([])
    
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = [[False] * m for _ in range(n)]
    
    덩어리_number = 1
    record = [[-1] * m for _ in range(n)]
    size = dict({})
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = True
                
                record[i][j] = 덩어리_number
                석유 = 1
                
                # bfs 시작 
                while queue:
                    y, x = queue.popleft()
                    
                    for direction in directions:
                        dy, dx = direction
                        ny = dy + y
                        nx = dx + x
                        if 0 <= ny < n and 0 <= nx < m:
                            if not visited[ny][nx] and land[ny][nx] == 1:
                                visited[ny][nx] = True
                                queue.append((ny, nx))
                                record[ny][nx] = record[i][j]
                                석유 += 1
                # bfs 끝 
                size[덩어리_number] = 석유
                덩어리_number += 1

    answer = []
    for i in range(m):
        arr = []
        for j in range(n):
            if record[j][i] != -1:
                arr.append(record[j][i])
        total_석유 = 0
        for element in list(set(arr)):
            total_석유 += size[element]
        answer.append(total_석유) 
    return max(answer)
    
                
        

    

