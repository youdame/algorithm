from collections import deque
def solution(board):
    
    n = len(board)
    m = len(board[0])
    start = ()
    target = ()
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start = (i, j)
            if board[i][j] == "G":
                target = (i, j)

                
    queue = deque([(start[0], start[1], 0)])
    visited = [[False] * m for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0
    while queue: 
        y, x, dist= queue.popleft()
        count += 1
        
        if (y, x) == target:
            return dist

        for dy, dx in directions:
            ny = y
            nx = x 

            while 0 <= ny + dy < n and 0 <= nx + dx < m and board[ny + dy][nx + dx] != "D":
                ny += dy
                nx += dx 
            if not visited[ny][nx]:
                queue.append((ny, nx, dist+1)) 
                visited[ny][nx] = True

    return -1
                
            
                
            
        