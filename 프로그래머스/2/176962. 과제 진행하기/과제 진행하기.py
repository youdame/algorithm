def calculate_minutes(start):
    hour, minute = map(int, start.split(":"))
    
    return hour * 60 + minute

def solution(plans):
    
    plans.sort(key = lambda x: x[1])

    
    times = []
    for i in range(len(plans)):
        name, start, playtime = plans[i]
        plans[i][1] = calculate_minutes(start)
        plans[i][2] = int(plans[i][2])
        times.append(plans[i][1])
    # print(plans)
    
    stack = []
    

    answer = []
    for i in range(len(plans) - 1):
        
        time_gap = plans[i+1][1] - plans[i][1]
        playtime = plans[i][2]
        
        if time_gap < playtime:
            stack.append((plans[i][0], playtime - time_gap))
        else:
            answer.append(plans[i][0])
            spare_time = time_gap - playtime
            
            while stack and spare_time > 0:
                name, remain_time = stack.pop()
                
                if remain_time <= spare_time:
                    answer.append(name)
                    spare_time = spare_time - remain_time
                else:
                    stack.append((name, remain_time - spare_time ))
                    spare_time = 0 

    answer.append(plans[-1][0])
       
    while stack:
        name, remain_time = stack.pop()            
        answer.append(name)
        
    return answer
        