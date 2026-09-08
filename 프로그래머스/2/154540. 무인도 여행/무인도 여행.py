from collections import deque

def solution(maps):    
    start = ()
    
    n = len(maps)
    m = len(maps[0])
    
    
    visited = [[False] * m for _ in range(n)]
    
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    answer = []
    for i in range(n):
        for j in range(m):
            
            if maps[i][j] != "X" and not visited[i][j]:
                queue = deque([(i, j)])
                sum_nums = int(maps[i][j])
                visited[i][j] = True
                while queue:
                    
                    y, x = queue.popleft()
                    

                    for dy, dx in directions:
                        ny = dy + y
                        nx = dx + x
                        if 0 <= ny < n and 0 <= nx < m :
                            if not visited[ny][nx] and maps[ny][nx] != "X":
                                visited[ny][nx] = True
                                queue.append((ny,nx))
                                sum_nums += int(maps[ny][nx])

                answer.append(sum_nums)
    return sorted(answer) if answer else [-1]


