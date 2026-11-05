def solution(numbers, target):

    
    n = len(numbers)
    answer = 0
    
    def dfs(x, index ):
        nonlocal answer
        
        if index == n:
            # print(x)
            if x == target:
                answer += 1
            return 
        
        
        # +를 붙인 경우
        dfs(x + numbers[index], index+1)
        # -를 붙인 경우 
        dfs(x - numbers[index], index+1)
    dfs(0, 0)
    return answer