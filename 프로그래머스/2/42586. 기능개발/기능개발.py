from collections import deque

import math
def solution(progresses, speeds):
    
    n = len(progresses)
    days = [math.ceil((100 - progresses[i]) / speeds[i])  for i in range(n) ]
    
    days = deque(days)
    
    
    answer = []
    
    count = 0
    
    max_day = days[0]
    
    for day in days:
        if day <= max_day:
            count += 1
        else:
            answer.append(count)
            max_day = day
            count = 1
    answer.append(count)
    return answer
    
        
    