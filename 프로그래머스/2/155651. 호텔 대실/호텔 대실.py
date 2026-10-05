import heapq


def get_minutes(str_time):
    hours, minutes = map(int, str_time.split(":"))
    
    return hours * 60 + minutes
def solution(book_time):
    book_time = sorted([(get_minutes(start), get_minutes(end)) for start, end in book_time])
    """
    지금 있는 방 중에 들어갈 수 있는 방이 있는지를 확인하는데에 힙을 사용한다..
    즉, 사용하는 방을 담는다
    사용하는 방 중 가장 빨리 퇴실하는 방을 알려주는 거임 그러니 확인은 한 번만 해도 됨
    
    """
    
    heap = []
    answer = 0
    # print(book_time)
    
    for start, end in book_time:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, (end + 10))


    return len(heap)

            
            
            
    