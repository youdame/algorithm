from itertools import permutations
def solution(expression):
    
    
    operator = ["+", "*", "-"]
    
    n = len(expression)
    
    op_stack = []
    num_stack = []
    num = ""
    
    for i in range(n):
        
        k = expression[i]
        if k in operator:
            op_stack.append(k)
            num_stack.append(int(num))
            num = ""
            
        else:
            num += k
            
    num_stack.append(int(num)) 
    print(num_stack, op_stack)
    
    answer = 0
    for per in permutations(operator):
        curr_nums = num_stack[:]
        curr_ops = op_stack[:]

        for op in per:
            new_nums = [curr_nums[0]]
            new_ops = []
            
            for i in range(len(curr_ops)):
                curr_op = curr_ops[i]
                if curr_op == op:
                    prev_num = new_nums.pop()
                    nxt_num = curr_nums[i+1]
                    if op == "+" : result = prev_num + nxt_num   
                    elif op == "-" : result = prev_num - nxt_num   
                    elif op == "*" : result = prev_num * nxt_num   
                    new_nums.append(result)
                else:
                    new_nums.append(curr_nums[i+1])
                    new_ops.append(curr_ops[i])
            curr_nums = new_nums
            curr_ops = new_ops
            
        answer = max(answer, abs(curr_nums[0]))    
    return answer
    
    