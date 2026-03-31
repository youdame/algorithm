import sys
from io import StringIO
from collections import deque


N, L, R = map(int, input().split()) 

A = []

for _ in range(N):     
    A.append(list(map(int, input().split()) ))


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def print_A():
    print(A)
def bfs(node, visited):
    
    i, j = node
    queue = deque([node])
    visited[i][j] = True
    
    team_total_people_count = A[i][j]
    team_node = [(i, j)]
    
    
    while queue:
        y, x = queue.popleft()
        
        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx] and L <= abs(A[y][x] - A[ny][nx]) <= R:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                    team_node.append((ny,nx))
                    team_total_people_count += A[ny][nx]


    if len(team_node) > 1:
        for member in team_node:
            mi, mj= member
            A[mi][mj] =  team_total_people_count // len(team_node)  
        
        return True
    return False

answer = 0

# 더이상 돌 수 없을 때까지 
while True:
    visited = [[False] * N for _ in range(N)]

    possible = False

    # 하루 
    for i in range(N):
        for j in range(N):
            # 밖에서 순회가 가능한지 계산하는 게 아니라 안에서 계산하고 넘겨주기 
            if not visited[i][j]:
                if bfs((i, j), visited):
                    possible = True
                
    if not possible: 
        break
    else:
        answer += 1
print(answer)
