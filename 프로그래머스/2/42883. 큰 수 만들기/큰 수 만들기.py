def solution(number, k):
  
    stack = []
    
    temp = k
    for i in range(len(number)):
        num = number[i]

        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1

        stack.append(num)

    if k > 0:
        stack = stack[:-k]
    
        
    return "".join(stack)
            