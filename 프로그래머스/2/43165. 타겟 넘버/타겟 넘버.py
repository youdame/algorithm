def solution(numbers, target):
    
    path = []
    
    n = len(numbers)
    
    answer = 0
    def backtrack():
        nonlocal answer
        if len(path) == n:
            result = 0
            for i in range(n):
                result += path[i] * numbers[i]

            if result == target:
                answer += 1
            return 
        
        for 부호 in (-1, 1):
            path.append(부호)        
            backtrack()
            path.pop()
    backtrack()
    return answer
    
    
    