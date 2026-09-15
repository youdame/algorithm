from collections import deque

def solution(A, B):
    A.sort()
    B.sort()
    
    
    queue_A = deque(A)
    queue_B = deque(B)
    
    
    
    n = len(A)
    
    start = 0
    
    answer = 0
    
    count = 0
    while start < n:
        if count >= n:
            return answer
        if queue_A[start] < queue_B[start]:
            start += 1
            answer += 1
        else:
            queue_B.append(queue_B.popleft())
        count += 1
#     print(queue_A)
#     print(queue_B)
        
    return answer 
        
        