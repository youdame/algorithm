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
        elif alpha == "D":
            
            if not min_heap:
                continue            
            if num == -1:
                pop_node = heapq.heappop(min_heap)
                max_heap.pop(max_heap.index(-1 * pop_node))
            elif num == 1:
                pop_node = -heapq.heappop(max_heap)
                min_heap.pop(min_heap.index(pop_node))

    if not min_heap:
        return [0, 0]    

    return [-max_heap[0], min_heap[0]]