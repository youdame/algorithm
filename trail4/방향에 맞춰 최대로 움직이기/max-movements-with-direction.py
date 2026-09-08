n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.

directions = [(-1, 0),  (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


stack = [(r,c)]


"""
시작점에서 갈 수 있는 가능성이 있는 좌표를 찾아

"""



r = r - 1
c = c - 1



answer = 0
def backtrack(current_r, current_c, cnt):
    global answer
    answer = max(answer, cnt)


    dy, dx = directions[move_dir[current_r][current_c] - 1]

    ny = current_r
    nx = current_c

    while 0 <= nx + dx < n and 0 <= ny + dy < n:
        ny += dy
        nx += dx

        
        if num[ny][nx] > num[current_r][current_c]:
            backtrack(ny, nx, cnt + 1)

backtrack(r, c, 0)    
print(answer)
