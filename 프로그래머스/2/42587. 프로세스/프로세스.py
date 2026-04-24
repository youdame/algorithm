"""
우선순위 큐면 heap을 써야하나?
heap은 pop을 하면 내부적으로 재정렬을 하나?

"""
from collections import deque

def solution(priorities, location):
    
    queue = deque([])
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
    
    priorities.sort(reverse=True)
    count = 0
    
    while queue:
        process, index = queue.popleft()
        
        
        if priorities[0] > process:
            queue.append((process, index))
        else:
            count += 1
            priorities.pop(0)
            if index == location:
                return count
            
            
