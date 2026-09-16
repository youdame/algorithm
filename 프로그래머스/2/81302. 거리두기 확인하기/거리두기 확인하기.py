
from collections import deque
def solution(places):
    answer = []
    for place in places:
        # print(place)
        
        p_set = set() 
        for y in range(5):
            for x in range(5):
                
                if place[y][x] == "P":
                    p_set.add((y,x))
                    
        
        is_ok = True
        for y in range(5):
            for x in range(5):
                
                if place[y][x] == "P":
                    # print(y,x)
                    visited = [[-1] * 5 for _ in range(5)]
                    queue = deque([(y, x)])
                    visited[y][x] = 0
                    
                    while queue:
                        r, c = queue.popleft()
                        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                            ny = dy + r
                            nx = dx + c
                            if 0 <= ny < 5 and 0 <= nx < 5 and place[ny][nx] != "X":
                                if visited[ny][nx] == -1 :
                                    visited[ny][nx] = visited[r][c] + 1
                                    queue.append((ny, nx))
                # print(visited)
                    for r2, c2 in p_set:
                        if visited[r2][c2] != -1 and visited[r2][c2] <= 2 and visited[r2][c2] != 0:
                            is_ok = False
                    if not is_ok:
                        answer.append(0)
                        break 
                if not is_ok:
                    break 
            if not is_ok:
                break 
            
        if is_ok:
            answer.append(1)
            
    return answer