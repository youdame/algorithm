def solution(numbers):
    n = len(numbers)
    
    stack = []
    new_max = 0
    answer = [-1] * n
    
    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            new_max = numbers[i]
            answer[stack.pop()] = new_max
        
        stack.append(i)
                
    return (answer)                
            