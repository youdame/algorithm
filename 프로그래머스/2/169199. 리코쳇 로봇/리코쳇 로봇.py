from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])

    G_loc = ()
    R_loc = ()
    for i in range(n):
        for j in range(m):
            if board[i][j] == "G":
                G_loc = (i, j)
            if board[i][j] == "R":
                R_loc = (i, j)
    
    r_r, r_c = R_loc
    g_r, g_c = G_loc
    queue = deque([(r_r, r_c)])
    
    dist = [[-1] * m for _ in range(n)]
    dist[r_r][r_c] = 0
    while queue:
        y, x = queue.popleft()
        
        if y == g_r and x == g_c:
            return dist[g_r][g_c]
        
        for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            ny = y
            nx = x
            while 0 <= ny + dy < n and 0 <= nx + dx < m and board[ny+dy][nx+dx] != "D":
                ny += dy
                nx += dx
            if dist[ny][nx] == -1 :
                dist[ny][nx] = dist[y][x] + 1
                queue.append((ny, nx))
        
    return -1
    
        