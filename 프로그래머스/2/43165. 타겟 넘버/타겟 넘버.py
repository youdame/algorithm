def solution(numbers, target):

    
    n = len(numbers)
    answer = 0
    
    def dfs(x, count, index ):
        nonlocal answer
        
        if count == n:
            # print(x)
            if x == target:
                answer += 1
            return 
        
        
        # +를 붙인 경우
        dfs(x + numbers[index], count+1, index+1)
        # -를 붙인 경우 
        dfs(x - numbers[index], count+1, index+1)
    dfs(0, 0, 0 )
    return answer