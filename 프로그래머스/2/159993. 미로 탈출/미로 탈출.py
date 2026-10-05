from collections import deque

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def solution(maps):
    
    record = dict()
    
    n = len(maps)
    m = len(maps[0])


    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                record["S"] = (i, j)
                
            elif maps[i][j] == "E":
                record["E"] = (i, j)
            elif maps[i][j] == "L":
                record["L"] = (i, j)

    s_y, s_x = record["S"]
    l_y, l_x = record["L"]
    e_y, e_x = record["E"]
    
    
    queue = deque([(s_y, s_x)])
    distance = [[-1] * m for _ in range(n)]
    distance[s_y][s_x] = 0
    answer = 0
    while queue:
        y, x = queue.popleft()  
        if l_y == y and l_x == x:
            answer = distance[l_y][l_x]
            break 
        for dy, dx in directions:
            ny = dy + y
            nx = dx + x
            
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X" :
                if distance[ny][nx] == -1:
                    queue.append((ny, nx))
                    distance[ny][nx] = distance[y][x] + 1
    
    if (distance[l_y][l_x]) == -1:
        return -1
    
    queue = deque([(l_y, l_x)])
    distance = [[-1] * m for _ in range(n)]
    distance[l_y][l_x] = 0
    
    while queue:
        y, x = queue.popleft()  
        if e_y == y and e_x == x:
            answer += distance[e_y][e_x] if distance[e_y][e_x] != -1 else 0
            break 
        for dy, dx in directions:
            ny = dy + y
            nx = dx + x
            
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X" :
                if distance[ny][nx] == -1:
                    queue.append((ny, nx))
                    distance[ny][nx] = distance[y][x] + 1
    
    if (distance[e_y][e_x]) == -1:
        return -1
    
    return answer    