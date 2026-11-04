from collections import deque

import math
def solution(progresses, speeds):
    
    n = len(progresses)
    days = [math.ceil((100 - progresses[i]) / speeds[i])  for i in range(n) ]
    
    days = deque(days)
    
    
    answer = []
    
    # print(possible_배포일)

    while days:
        day = days.popleft()
        count = 1
        
        while days and days[0] <= day:
            count += 1
            days.popleft()
        if count > 0:
            answer.append(count)
    return answer
    
        
    