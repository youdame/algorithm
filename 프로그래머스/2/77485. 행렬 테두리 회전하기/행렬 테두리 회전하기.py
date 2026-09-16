def solution(rows, columns, queries):
    grid = [[j + i * columns for j in range(1, columns+1) ]for i in range(rows)]
    

    answer = [ ]
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        arr = []
        temp = grid[x1][y1]
        
        
        
        # 왼쪽
        
        for i in range(x1+1,x2+1):
            # j는 b로 고정
            grid[i-1][y1] = grid[i][y1]
            arr.append(grid[i][y1])
        
        
        # 아래쪽 
        for j in range(y1+1,y2+1):
            grid[x2][j-1] = grid[x2][j]
            arr.append(grid[x2][j])

        # print("아래쪽 ", grid)
        # 오른쪽  
        for i in range(x2, x1, -1):
            grid[i][y2] = grid[i-1][y2]
            arr.append( grid[i-1][y2])
        # print("오른쪽 ", grid)
        # 위쪽 
        for j in range(y2, y1, -1):
            grid[x1][j] = grid[x1][j-1]
            arr.append(grid[x1][j-1])
        # print("위쪽 ", grid)
        grid[x1][y1+1] = temp
        arr.append(temp)
        
        answer.append(min(arr))
        
    return answer