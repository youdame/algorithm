def solution(number, k):
    stack = []
    
    n = len(number)
    for i in range(n):
        while k > 0 and stack and stack[-1] < number[i]:
            stack.pop()
            k -= 1 
        
        stack.append(number[i])
        
    if k > 0:
        stack = stack[:len(stack) - k]
    return "".join(stack)