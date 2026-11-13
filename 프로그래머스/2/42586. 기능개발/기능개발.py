import math
from collections import deque
def solution(progresses, speeds):
    n = len(progresses)
    remain_work = [0] * n
    
    for i in range(n):
        remain_work[i] = math.ceil((100- progresses[i]) / speeds[i])
    remain_work = deque(remain_work)
    answer =[]
    print(remain_work)
    while remain_work :
        work = remain_work.popleft()
        count = 1
        while remain_work and remain_work[0] <= work:
            remain_work.popleft()
            count += 1            
        answer.append(count)
    return answer