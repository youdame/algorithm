

def solution(prices):
    
    
    stack = []
    answer = [0] * len(prices)

    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            pop_time = stack.pop()
            answer[pop_time] = i - pop_time
        
        stack.append(i)
        

    while stack:
        pop_time = stack.pop()
        answer[pop_time] = i - pop_time
        
    return answer
        

