import sys
from collections import deque 
input = sys.stdin.readline
N, M, K = map(int, input().split())


sea_matrix = [list(map(int, input().split())) for _ in range(N)]

# [y, x]
tutle_location = [list(map(int, input().split())) for _ in range(M)]

# (r, c, P, 현재 압력)
fire_status = [list(map(int, input().split())) +[0] for _ in range(K)]
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

answer = [-1] * M


# 2. 거북이 상태 
is_dead = [False] * M       # 화석화 여부
is_escaped = [False] * M    # 도착 여부

def move(turn_number):

    def bfs(cur_idx):
            distance = [[1e9] * N for _ in range(N)]
            queue = deque([(N - 1, N - 1)])
            distance[N - 1][N - 1] = 0

            # 장애물 맵 만들기 (산호초 + 화석 + '다른' 살아있는 거북이)
            blocked = [[False] * N for _ in range(N)]
            
            # (1) 산호초 및 화석(1)을 벽으로 등록
            for r in range(N):
                for c in range(N):
                    if sea_matrix[r][c] == 1:
                        blocked[r][c] = True

            # (2) 나를 제외한 '다른 살아있는 거북이'만 벽으로 등록
            for idx in range(M):
                if idx != cur_idx and not is_dead[idx] and not is_escaped[idx]:
                    tr, tc = tutle_location[idx]
                    blocked[tr][tc] = True

            # BFS 거리 탐색
            while queue:
                y, x = queue.popleft()

                for dy, dx in directions:
                    ny = y + dy
                    nx = x + dx
                    # 맵 범위 안이고, 아직 방문 안 했고, 장애물이 아니라면 진행
                    if 0 <= ny < N and 0 <= nx < N :
                        if not blocked[ny][nx] and distance[ny][nx] == 1e9:
                            distance[ny][nx] = distance[y][x] + 1
                            queue.append((ny, nx))
                            
            return distance

    def each_move(i, tutle):

        y, x = tutle
        distance = bfs(i)
        min_dist = distance[y][x]

        # 최단 경로가 존재하지 않는다면 제자리
        direction = (0, 0)

        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1,0)]:

            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < N and distance[ny][nx] != 1e9 and distance[ny][nx] < min_dist:
                min_dist = distance[ny][nx]
                direction = (dy, dx)


        tutle_location[i] =[y + direction[0], x + direction[1]]
        
    



    for i in range(M):
        if not is_dead[i] and not is_escaped[i]:
            each_move(i, tutle_location[i]) 


        # 안식처 도착 
        if tutle_location[i] == [N-1, N-1]:
            answer[i] = turn_number
            # 후 처리 해야할듯..? 거북이 위치 어떻게 설정..? 
            tutle_location[i] = [-1, -1]
            is_escaped[i] = True


def charge():
    for i in range(K):
        fire_status[i][3] += 10 

def eruption():

    fire_matrix = [[0] * N for _ in range(N)]

    def propagation(r, c, P):
        fire_matrix[r][c] += P
        for dy, dx in directions:
            fire = P // 2
            ny = r + dy
            nx = c + dx
            while fire > 0:
                if 0 <= ny < N and 0 <= nx < N and sea_matrix[ny][nx] == 0 :
                    
                    fire_matrix[ny][nx] += fire
                    ny += dy
                    nx += dx 
                    fire = fire // 2
                else:
                    break

                


    def chain_react():

        erupted = [False] * K  

        while True:
            has_new_eruption = False
            for i in range(K):
                if not erupted[i]:
                    r, c, P, current_fire = fire_status[i]
                    if current_fire + fire_matrix[r][c] >= P:
                        erupted[i] = True
                        has_new_eruption = True
                        propagation(r, c, P)

            if not has_new_eruption:
                break
                
        return erupted


    def dead():
        for i in range(M):
            if not is_dead[i] and not is_escaped[i]:
                r, c = tutle_location[i]
                
                if fire_matrix[r][c] >= 20 and not is_dead[i] and not is_escaped[i]:
                    is_dead[i] = True
                    sea_matrix[r][c] = 1


    erupted = chain_react()
    dead()
    return erupted

def reset(erupted):
    for i in range(K):
        if erupted[i]:
            fire_status[i][3] = 0
            



def print_all(turn_number):

    # print(f"=======turn {turn_number}=========")
    # print("거북이 위치 :" , tutle_location)
    # print("화산 상태 : ",  fire_status)

    print("거북이 상태", is_dead)
    print("거북이 탈출 여부", is_escaped)
    print("answer : ", answer)
    # print(f"==================================")



for turn_number in range(1, 101):
    move(turn_number)

    charge()
    
    erupted = eruption()
    reset(erupted)
    # print_all(turn_number)

for i in range(M):
    print(answer[i])