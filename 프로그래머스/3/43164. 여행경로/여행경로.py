def solution(tickets):
    n = len(tickets)
    tickets.sort()
  
    arr = ["ICN"]
    visited= [False] * n
    
    answer = []
    
    def dfs(arr):
        if len(arr) == n + 1:
            answer.append(arr[:])
            return 
        
        for i in range(n):
            a, b = tickets[i]
            if a == arr[-1] and not visited[i]:
                arr.append(b)
                visited[i] = True
                dfs(arr)
                arr.pop()
                visited[i] = False
    dfs(arr)

    return answer[0]