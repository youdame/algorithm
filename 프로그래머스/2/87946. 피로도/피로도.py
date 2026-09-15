def solution(k, dungeons):
    
    
    path = []
    n = len(dungeons)
    possible_path = []
    
    
    def backtrack():
        if len(path) == n:
            possible_path.append(list(path))
            return 
        
        for i in range(n):
            if i not in path:
                path.append(i)
                backtrack()
                path.pop()

    backtrack()
    
    answer = 0
    for path in possible_path:
        hp = k
        count = 0
        for idx in path:
            최소, 소모 = dungeons[idx]
            if hp < 최소:
                break
            else:
                
                hp -= 소모
                count += 1
        answer = max(answer, count)
    return answer