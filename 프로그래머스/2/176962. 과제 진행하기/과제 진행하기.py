def solution(plans):
    
    plans.sort(key = lambda x : x[1])
    n = len(plans)
    

    for i in range(len(plans)):
        name, start, playtime = plans[i]
        hour, minutes = map(int, start.split(":"))    
        start = hour * 60 + minutes
        plans[i] = [name, start, int(playtime)]
        
    
    """ 
    멈춘 과제의 이름, 시간
    멈춘 과제의 배열이 비어있는지 아닌지
    지금 가능한지 
    """
    answer = []
    stack = []
    


    for i in range(n-1):

        name, start, playtime = plans[i]
        next_start = plans[i+1][1]
        
        finish = start + playtime
        

        if finish > next_start:
            stack.append([name, finish - next_start])
        else:
            answer.append(name)
            gap = next_start - finish
            while stack and gap > 0:
                remain_name, remain_playtime = stack[-1]
                if remain_playtime <= gap: 
                    stack.pop()
                    answer.append(remain_name)
                    gap -= remain_playtime
                else:
                    stack[-1][-1] -= gap
                    gap = 0
                    
    answer.append(plans[-1][0])
    while stack:
        answer.append(stack.pop()[0])
            
                        
        
    return answer
    
        