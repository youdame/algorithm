from collections import defaultdict

def solution(tickets):
    
    adj = defaultdict(list)
    
    tickets.sort(key = lambda x : x[1], reverse = True)
    # print(tickets)
    for start, end in tickets:
        adj[start].append(end)
    # print(adj)
        
        
    
    stack = ["ICN"]
    
    answer = []

    while stack:
        
        top = stack[-1]
        
        if adj[top]:
            stack.append(adj[top].pop())
        else:
            answer.append(stack.pop())
            


    return answer[::-1]