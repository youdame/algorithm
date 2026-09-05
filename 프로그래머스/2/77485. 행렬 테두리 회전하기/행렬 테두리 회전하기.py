def solution(rows, columns, queries):
    
    
    grid = [[i * columns + j for j in range(1, columns + 1)] for i in range(rows)]
    
    
    queries = [[a-1, b-1, c-1, d-1] for a, b , c, d in queries]
    
    answer= []
    for query in queries:
        x1, y1, x2, y2 = query
        top_left = grid[x1][y1]
        min_val = top_left
        
        # 왼
        
        for x in range(x1, x2):
            grid[x][y1] = grid[x+1][y1] 
            min_val = min(min_val, grid[x][y1])
        # 아 
        for y in range(y1, y2):
            grid[x2][y] = grid[x2][y+1]
            min_val = min(min_val, grid[x2][y])
                
        # 오 
        for x in range(x2, x1, -1):
            grid[x][y2] = grid[x-1][y2]
            min_val = min(min_val, grid[x][y2])
            
        # 위
        for y in range(y2, y1+1, -1):
            grid[x1][y] = grid[x1][y-1]
            min_val = min(min_val, grid[x1][y])
            
        grid[x1][y1 + 1] = top_left
        answer.append(min_val)
        
    return answer