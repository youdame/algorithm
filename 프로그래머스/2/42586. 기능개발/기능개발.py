from collections import deque
import math
"""
일단 며칠만에 완료됐는지를 적어놓고, 배포가 가능한 애들을 배포함 
"""

def solution(progresses, speeds):
    queue = deque([])
    n = len(progresses)
    
    for i in range(n):
        remain = 100 - progresses[i]
        work_days = math.ceil(remain / speeds[i])
        queue.append(work_days)

    
    answer = []
    
    while queue:
        node = queue.popleft()
        count = 1
        while queue and node >= queue[0]:
            queue.popleft()
            count += 1
        answer.append(count)
    return answer