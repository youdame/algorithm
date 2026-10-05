from collections import deque

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def solution(maps):
    n, m = len(maps), len(maps[0])
    record = dict()
    for i in range(n):
        for j in range(m):
            if maps[i][j] in "SLE":
                record[maps[i][j]] = (i, j)

    s_y, s_x = record["S"]
    l_y, l_x = record["L"]
    e_y, e_x = record["E"]
    
    answer = 0
    
    
    def bfs(start, target):
        
        s_y , s_x = start
        t_y, t_x = target
        queue = deque([(s_y, s_x)])
        distance = [[-1] * m for _ in range(n)]
        distance[s_y][s_x] = 0
        answer = 0

        while queue:
            y, x = queue.popleft()  
            if t_y == y and t_x == x:
                answer = distance[t_y][t_x]
                break 
            for dy, dx in directions:
                ny = dy + y
                nx = dx + x

                if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X" :
                    if distance[ny][nx] == -1:
                        queue.append((ny, nx))
                        distance[ny][nx] = distance[y][x] + 1

        if (distance[t_y][t_x]) == -1:
            return -1
    
    
        return answer 
    
    
    s_l = bfs(record["S"], record["L"])
    l_e = bfs(record["L"], record["E"])
    
    if s_l == -1 or l_e == -1:
        return -1
    else:
        return s_l + l_e
  