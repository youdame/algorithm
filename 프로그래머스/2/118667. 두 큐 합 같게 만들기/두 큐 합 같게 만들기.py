from collections import deque
def solution(queue1, queue2):
    queue = deque(queue1 + queue2)
    left = 0
    right = len(queue1)
    
    cur_sum = sum(queue1)
    n = len(queue)
    
    
    one_sum = sum(queue) // 2
    count = 0
    while cur_sum != one_sum:
        if cur_sum > one_sum:
            cur_sum -= queue[left]
            left = (left + 1) % n
        elif cur_sum < one_sum:
            cur_sum += queue[right]
            right = (right + 1) % n
        else:
            break
        if count > 2 * n:
            return -1
        count += 1
    return count
    
            

    
    