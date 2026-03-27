import sys
from io import StringIO
import copy
"""
사각지대를 최소화한다 = 최대한 감시할 수 있는 만큼 하려면?
CCTV는 통과 가능, 6인 벽은 통과 X

여러 종류의 카메라가 여러 개 존재하면 어떻게 해야하는거지..? -> 가능한 경우의 수를 다 본다..
이 문제는 왜 백트래킹인가? 조합 + bfs로 풀면 안되는가? 

"""

input = sys.stdin.readline

n, m = map(int, input().split())
current_board = []


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_record = {}

direction_record[1] = [[0], [1], [2], [3]]
direction_record[2] = [[0, 2], [1, 3]]
direction_record[3] = [[0, 1], [1, 2], [2, 3], [3, 0]]
direction_record[4] = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
direction_record[5] = [[0, 1, 2, 3]]

for _ in range(n):
    current_board.append(list(map(int, input().split())))



camera_info = []
for i in range(n):
    for j in range(m):
        if current_board[i][j] in [1, 2, 3, 4, 5]:
            camera_info.append((current_board[i][j], i, j))


def watch(y, x, d_index_list, board):

    for index in d_index_list:
        ny = y
        nx = x
        dy, dx = directions[index]
        
        while True:
            ny += dy
            nx += dx 
            
            if not (0 <= ny < n and 0 <= nx < m):
                break

            if board[ny][nx] == 6:
                break

            if board[ny][nx] == 0:
                board[ny][nx] = -1
        

answer = 1e9
def backtrack(count, current_board):
    global answer
    if len(camera_info) == count:
        dont_watch_count = 0
        for i in range(n):
            for j in range(m):
                if current_board[i][j] == 0:
                    dont_watch_count += 1
        answer = min(dont_watch_count, answer)
        return

    
    
    # do 
    method, y, x = camera_info[count]
    
    for d_index_list in direction_record[method]:
        temp = copy.deepcopy(current_board)
        watch(y, x, d_index_list, temp)
    
        backtrack(count+1, temp)

    

backtrack(0, current_board)


print(answer)












