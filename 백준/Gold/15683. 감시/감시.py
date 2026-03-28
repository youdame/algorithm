import sys
from io import StringIO
import copy
"""
사각지대를 최소화한다 = 최대한 감시할 수 있는 만큼 하려면?
CCTV는 통과 가능, 6인 벽은 통과 X

여러 종류의 카메라가 여러 개 존재하면 어떻게 해야하는거지..? -> 가능한 경우의 수를 다 본다..

여러 개의 카메라의 경우의 수를 다 봐야함
=> 완전탐색
-> 완탐을 효율적으로 하는 법 백트래킹 ? 또 뭐있지? dp 이분탐색

"""
input = sys.stdin.readline

n, m = map(int, input().split())
current_board = []


for _ in range(n):
    current_board.append(list(map(int, input().split())))


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


d_index_record = {}

d_index_record[1] = [[0], [1], [2], [3]]
d_index_record[2] = [[0, 2], [1, 3]]
d_index_record[3] = [[0, 1], [1, 2], [2, 3], [3, 0]]
d_index_record[4] = [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]]
d_index_record[5] = [[0, 1, 2, 3]]

# (번호, y, x)
cctv_list = []
for i in range(n):
    for j in range(m):
        if current_board[i][j] in [1,2, 3,4,5]:
            cctv_list.append((current_board[i][j], i, j))


answer = 1e9

def watch(count, next_board):
    global answer
    # 재귀 종료 조건 
    if count == len(cctv_list):
        zero_count = 0
        for i in range(n):
            for j in range(m):
                if next_board[i][j] == 0:
                    zero_count += 1
        answer = min(zero_count, answer)   
        return
    
    
    # do
    # count에 해당하는 카메라 하나
    
    num, y, x = cctv_list[count]

    direction_indexes = d_index_record[num]



    
    # 한 카메라의 가능한 방향들     
    for d_index_list in direction_indexes:
        temp = copy.deepcopy(next_board)
        # 한 카메라의 각각의 방향들 
        for d_index in d_index_list:
            ny = y
            nx = x 
            # 하나의 방향에 대해서 쭉 가능한데까지 watch 
            dy, dx = directions[d_index]
            while True:
                ny += dy
                nx += dx 
                if not (0 <= nx < m and 0 <= ny < n):
                    break
                if temp[ny][nx] == 6:
                    break
                if temp[ny][nx] == 0:
                    temp[ny][nx] = -1
        # 다음 카메라 확인 
        watch(count+1, temp)
        
watch(0, current_board)

    
    
print(answer)

