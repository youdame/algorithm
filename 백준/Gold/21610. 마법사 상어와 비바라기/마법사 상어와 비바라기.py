import sys
from io import StringIO 


input = sys.stdin.readline

N, M = map(int, input().split())


# 새롭게 배운 마법 비바라기 -> 비구름 만들 수 있음
# A가 격자고 각 칸에 바구니가 있음, 바구니에는 물이 무한대로 들어갈 수 있음 
# A[r][c] => 물의 양
# 비바라기를 하면 4방향에 비구름이 생김 -> 구름은 칸 전체를 차지함 (5,1),(5,2), (4,1), (4, 2) -> -1씩 해야함 
# 구름의 이동을 M번 

A = [list(map(int, input().split())) for _ in range(N)]

moves= []

clouds = [(N - 1, 1 -1), (N-1, 2-1), (N-1-1, 1-1), (N-1-1, 2-1)]

        
directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0,1), (1, 1), (1, 0), (1, -1)]


for _ in range(M):
    d, s = map(int, input().split())

    dy, dx = directions[d-1]

    for i in range(len(clouds)):
        y, x = clouds[i] 
        
        new_y, new_x = (y + s * dy) % N, (x + s * dx) % N
        clouds[i] = (new_y, new_x)
        A[new_y][new_x] += 1

    rains = set(clouds)
    clouds = []

    
    for y, x in rains:
        for i in range(1, len(directions), 2):
            dy, dx = directions[i]
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < N and A[ny][nx] > 0:
                A[y][x] += 1
    for y in range(N):
        for x in range(N):
            if A[y][x] >= 2 and (y, x) not in rains:
                clouds.append((y, x))
                A[y][x] -= 2
answer = 0
for i in range(N):
    answer += sum(A[i])
print(answer)

        

        











