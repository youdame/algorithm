def time_to_minutes(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m


def solution(plans):
    
    plans = [[a, time_to_minutes(b), int(c)] for a, b, c in plans]
    
    plans.sort(key = lambda x : x[1])
    
    
    n = len(plans)
    stack = []
    
    answer = []
    for i in range(n-1):
        name, start, playtime = plans[i]
        next_name, next_start, next_playtime = plans[i + 1]
        
        if start + playtime > next_start :
            stack.append((playtime + start - next_start , name))
        else:
            answer.append(name)
            free_time = next_start - (start + playtime)             
            while free_time > 0 and stack:            
                remain_time, remain_name = stack.pop() 
                if remain_time - free_time > 0:
                    stack.append((remain_time - free_time, remain_name))
                else:
                    answer.append(remain_name)
                free_time -= remain_time
            
    answer.append(plans[-1][0])
    
    stack = [name for _, name in stack]
    print(answer + stack[::-1])
    return answer + stack[::-1] 