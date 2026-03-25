n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 3 * 3 

answer = -1e9
for y in range(n):
    possible = True
    for x in range(n):

        # 현 좌표에서 각각 2를 더한 값이 좌표 밖으로 벗어나선 안됨
        directions = [(0, 0), (0, 1), (0, 2), (1,0), (1, 1), (1, 2),(2, 0), (2, 1), (2, 2)]
        sum = 0
        if 0 <= x + 2 < n and 0 <= y + 2 < n:
            for dy, dx in directions:
                ny = y + dy
                nx = x + dx
                sum += grid[ny][nx]
       
        else:
            possible = False
            break
        answer = max(sum , answer)
    if not possible:
        break
        
print(answer)