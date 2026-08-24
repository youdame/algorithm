def solution(targets):
    
    targets.sort(key = lambda x : x[1])
    # print(targets)
    
    n = len(targets)
    count = 1
    
    current_target = targets[0][1]
    
    for index in range(1, n):
        
        x, y = targets[index]
        if x < current_target <= y:
            continue
        else:
            count += 1
            current_target = targets[index][1]
        # print(current_target)
    return count
        