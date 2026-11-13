from collections import deque
def solution(land):
    n = len(land)
    m = len(land[0])
    
    answer = -1e9

    visited = [[False] * m for _ in range(n)]
    oil_by_col = [0] * m
    
    for j in range(m):
        for i in range(n):
            if not land[i][j] or visited[i][j]:
                continue
            size = 0          # 현재 덩어리의 크기
            cols = set()      # 현재 덩어리가 걸쳐 있는 열 번호들

            queue = deque([(i, j)])
            visited[i][j] = True
            
            while queue:
                y, x = queue.popleft()
                cols.add(x)
                size += 1
                for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    ny = dy + y
                    nx = dx + x
                    if 0 <= ny < n and 0 <= nx < m :
                        if land[ny][nx] == 1 and not visited[ny][nx]:
                            visited[ny][nx] = True
                            queue.append((ny, nx))

            for col in cols:
                oil_by_col[col] += size
    # print(oil_by_col)
    return max(oil_by_col)            