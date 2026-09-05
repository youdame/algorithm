
from collections import deque
import math

def solution(queue1, queue2):
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    
    count = 0
    sum_q1 = sum(queue1)    
    sum_q2 = sum(queue2)
    
    while True:

        if count > 300000: 
            return -1
        if sum_q1 == sum_q2 :
            break
        elif sum_q1 > sum_q2:
            node1 = queue1.popleft()
            queue2.append(node1)
            sum_q1 -= node1
            sum_q2 += node1
            
        else:
            node2= queue2.popleft()
            queue1.append(node2)
            sum_q2 -= node2
            sum_q1 += node2
        count +=1 

    
    # print(sum(queue1 + queue2))
    return count
    

    