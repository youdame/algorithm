


def solution(m, n, board):
    answer = 0
    def is_range(y, x):
        return 0 <= y < m and 0 <= x < n
    def is_all_range(y, x):
        return is_range(y, x) and is_range(y + 1, x) and is_range(y, x + 1) and is_range(y + 1, x + 1)

    def is_all_same(y, x):
    # 빈칸이 아니면서, 4개의 블록이 모두 같은지 확인
        return board[y][x] != "" and (board[y][x] == board[y + 1][x] == board[y][x + 1] == board[y + 1][x + 1])

    
    
    
    # m, n을 다시 계산해야함.. 
    new_board = [[board[i][j] for j in range(n) ] for i in range(m)]
    
    
    while True:
        matched = set()

        for y in range(m):
            for x in range(n):
                if is_all_range(y, x):
                    if is_all_same(y, x):
                        matched.add((y, x))
                        matched.add((y + 1, x))
                        matched.add((y, x + 1))
                        matched.add((y + 1, x + 1))
        if not matched:
            break

        answer += len(matched)
        for y, x in matched:
            new_board[y][x] = ""

        # 수정 후
        for y in range(m - 1, -1, -1):  # 바닥(m-1)부터 천장(0)까지 역순 탐색
            for x in range(n):
                if new_board[y][x] != "":
                    ny, nx = y, x
                    while is_range(ny + 1, nx) and new_board[ny + 1][nx] == "":
                        ny += 1

                    if ny != y:  # 실제로 아래로 떨어졌을 때만 이동
                        new_board[ny][nx] = new_board[y][x]
                        new_board[y][x] = ""
        board = list(new_board)
    return answer