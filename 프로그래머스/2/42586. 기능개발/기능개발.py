from collections import deque

import math
def solution(progresses, speeds):
    
    n = len(progresses)
    possible_배포일 = [math.ceil((100 - progresses[i]) / speeds[i])  for i in range(n) ]
    
    possible_배포일 = deque(possible_배포일)
    
    
    answer = []
    day = possible_배포일[0]
    # print(possible_배포일)

    while possible_배포일:
        count = 0
        while possible_배포일 and possible_배포일[0] <= day:
            possible_배포일.popleft()
            count += 1
        day += 1
        if count > 0:
            answer.append(count)
    return answer
    
        
    