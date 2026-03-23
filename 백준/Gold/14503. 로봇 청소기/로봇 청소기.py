import sys
from io import StringIO 
input = sys.stdin.readline

N, M = map(int, input().split())

r,c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

count = 0

y = r
x = c
robot_direction = d


while True:
    if arr[y][x] == 0:
        count += 1 
        arr[y][x] = 2

    possible = False

    for i in range(4):
        # 반시계 방향 회전 
        robot_direction = (robot_direction - 1) % 4
        dy, dx = directions[robot_direction]

        ny = dy + y
        nx = dx + x
        if arr[ny][nx] == 0:
            possible = True
            y = ny
            x = nx 
            break
            
    if not possible:
        back_y, back_x = directions[(robot_direction + 2) % 4]
        ny = y + back_y
        nx = x + back_x
        if arr[ny][nx] == 1:
            break
        else:
            y = ny
            x = nx
print(count)
            
        
        



