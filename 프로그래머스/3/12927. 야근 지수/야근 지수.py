import heapq
def solution(n, works):
    
    works = [-x for x in works]
    
    heapq.heapify(works)
    
    i = 0
    while i < n:
        
        max_work = -heapq.heappop(works)
        
        max_work = max(0, max_work - 1)
        
        heapq.heappush(works, -max_work)
        
        i += 1
    return sum([work**2 for work in works])