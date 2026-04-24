import heapq
from collections import deque
def solution(priorities, location):
    
    heap = []
    
    
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    for element in priorities :
        heapq.heappush(heap, (-element))

    count = 0 
    while queue:
        p, i = queue.popleft()

        if p != -heap[0]:
            queue.append((p , i ))
        else: 
            count += 1
            if i == location : 
                return count
            heapq.heappop(heap)
    