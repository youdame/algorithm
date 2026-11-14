def solution(diffs, times, limit):    
    n = len(diffs)
    
    left = 1
    right = max(diffs)
    
    answer = max(diffs)
    
    while left < right:
        level = (left + right) // 2
        
        time = 0 
        
        for i in range(n):
            if diffs[i] <= level:
                time += times[i]
            else:
                time += (times[i-1] + times[i]) * (diffs[i]- level) + times[i]
            if time > limit:
                break
        # print(level, time)  
        if time <= limit:
            right = level 
            answer = min(answer, level)
        else:
            left = level + 1
    return answer