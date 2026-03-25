import sys 
from io import StringIO
from itertools import combinations
from collections import deque
import copy 
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list( map(int, input().split())))

"""
바이러스가 유출된 상태 
확산을 막기 위해 연구소에 벽을 세우려고 한다

연구소 = 빈칸, 벽, 바이러스으로 이뤄짐 (0, 1, 2)

벽을 세우지 않으면 바이러스가 상하좌우로 퍼짐
3개의 벽을 세워서 바이러스가 최대한 퍼지지 않게 하기 
"""

empty_locations = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty_locations.append((i, j))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(temp):
    # 한 번에 다 넣기 때문에 visited처리가 필요 없음 
    while queue:
        y, x = queue.popleft() 
        # 감염 처리 
        temp[y][x] = 2 
        
        for dy, dx in directions:
            ny, nx = dy+y, dx+x
            if 0 <= ny < N and 0 <= nx < M:
                if temp[ny][nx] == 0:
                    queue.append((ny, nx))
                    
                    

answer = 0

# 조합으로 3개 뽑기 
for comb in combinations(empty_locations, 3):

    queue = deque([])
    
    # 원본 배열을 보존하기 위해 copy
    # copy 문법 익히기 
    temp = copy.deepcopy(arr) 
    
    # 벽 세우기 
    for ey, ex in comb:
        temp[ey][ex] = 1
    
    # 바이러스마다 bfs 시작 
    for y in range(N):
        for x in range(M):
            # 바이러스는 한 번에 여러개 퍼지는 거니까.. 그냥 다 큐에 넣기
            if temp[y][x] == 2:
                queue.append((y, x))
    bfs(temp)
    

    # 안전 영역 계산 
    safe_area = 0            
    for y in range(N):
        for x in range(M):
            if temp[y][x] == 0:
                safe_area += 1
    
    answer = max(safe_area, answer)
    
print(answer)
    

