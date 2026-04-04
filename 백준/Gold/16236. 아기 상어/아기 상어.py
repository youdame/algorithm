import sys
from collections import deque
from io import StringIO
"""
N * N 공간  = arr
물고기 M마리, 아기상어 1마리
한 칸에 물고기 한 마리~

목표 : 엄마한테 도움요청하지 않고 잡아먹을 수 있는 시간 -> 걍 먹을 수 있을 때까지 먹어라

아기상어보다 크기가
큰 물고기 - 지나갈 수 X
같은 물고기 - 지나갈 수 O, 먹기 X
작은 물고기 - 지나갈 수 O 먹기 O

어디로 이동할까?
1) 더이상 먹을 수 있는 물고기가 없으면 엄마한테 도와줘
2) 먹을 수 있는 물고기 개수에 따라
- 한 마리면, 먹으러감
- 더 많으면, 가까운 물고기 먹으러 
=> 아기상어가 물고기 있는 칸으로 갈건데 지나가야하는 칸의 최솟값
거리가 가까운 애들이 많으면 가장위 -> 가장 왼쪽 순서대로 정렬해서 가져오기 

이동은 1초, 먹는데는 시간 안걸림
=> bfs

아기상어는 자기 몸무게만큼 먹으면 크기가 1증가함
"""


input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))


"""
1. 가까운 물고기 위치 찾기
- 자기보다 작아야함
- bfs 돌면서 찾으면 됨
    - 작거나, 같은 애들 경로로 해서 찾아가기
2. 가까운 물고기들 정렬해서 가장 우선순위인 애 먹기
3. 몸무게 증가 고려하기 
=> 먹을 수 있는 애가 없을 떄까지 반복
=> 시뮬레이션
"""

shark_location = ()
shark_weight = 2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark_location = (i, j)


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(node, distances, visited):
    can_eat_fishes = []
    i, j = node
    visited[i][j] = True
    distances[i][j] = 0
    queue = deque([node])
    
    while queue:
        y, x = queue.popleft()

        for dy, dx in directions:
            ny, nx = dy + y, dx + x
            # 방문 안했고, 범위 안에 있꼬 
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] :
                # 내가 지나갈 수 있는 
                if arr[ny][nx] <= shark_weight:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                    distances[ny][nx] = distances[y][x] + 1

                # 빈칸이 아니고 내가 먹을 수 있는 물고기 
                if arr[ny][nx] != 0 and arr[ny][nx] < shark_weight:
                    can_eat_fishes.append((ny, nx))
    return can_eat_fishes

answer = 0
ate_fishes_count = 0

while True:
    distances = [[1e9] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    
    can_eat_fishes = bfs(shark_location, distances, visited)
    
    # 더이상 먹을 수 있는 게 없으면 break
    if len(can_eat_fishes) == 0:
        break
    
    # 먹을 수 있는 물고기가 한 마리일 때, 여러 마리일 때,,,, 
    sorted_can_eat_fishes = sorted(can_eat_fishes, key = lambda x : (distances[x[0]][x[1]], x[0], x[1]))

    i, j = sorted_can_eat_fishes[0]
    answer += distances[i][j]
    # 물고기 죽음 
    arr[i][j] = 0

    # 상어 위치, 먹은 물고기 수 업데이트 
    arr[shark_location[0]][shark_location[1]] = 0
    shark_location = (i, j)
    ate_fishes_count += 1

    if ate_fishes_count == shark_weight:
        shark_weight += 1
        ate_fishes_count = 0
        

print(answer)
    










            


