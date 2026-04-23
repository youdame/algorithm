from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    
    future = deque(truck_weights)

    current = deque([])
    times = deque([])

    
    while future or current:
    
        if current and times and time - times[0] == bridge_length:
            current.popleft()
            times.popleft()
            
        if future and sum(current) + future[0] <= weight:
            current.append(future.popleft())
            times.append(time)


        # print(times, time, current, future)
        
        time += 1

    return time 
            