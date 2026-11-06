import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    
    for operation in operations:
        alpha, num = operation.split(" ")
        num = int(num)
        if alpha == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif alpha == "D" and min_heap:            
            if num == -1:
                pop_node = heapq.heappop(min_heap)
                max_heap.pop(max_heap.index(-1 * pop_node))
            elif num == 1:
                pop_node = -heapq.heappop(max_heap)
                min_heap.pop(min_heap.index(pop_node))
    return [ max(min_heap) if max_heap else 0,min(min_heap) if min_heap else 0]