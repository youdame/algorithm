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

    r, c = R_loc
    queue = deque([(r, c, 0)])

    visited= [[False] * m for _ in range(n)] 
    visited[r][c] = True
    
    while queue:
        y, x, dist = queue.popleft()
        if y == G_loc[0] and x == G_loc[1]:
            return dist
     
        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ny = y
            nx = x 
            while 0 <= ny + dy < n and 0 <= nx + dx < m and board[ny + dy][nx +dx] != "D":
                ny += dy 
                nx += dx 
            if not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny,nx, dist+1))
    return -1