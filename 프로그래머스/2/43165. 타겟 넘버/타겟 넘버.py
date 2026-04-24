import sys
sys.setrecursionlimit(2000)

def solution(numbers, target):
    n = len(numbers)
    
    arr = []
    count = 0
    def backtracking():
        nonlocal count
        if len(arr) == n:
            result = 0
            for i in range(n):
                result += arr[i] * numbers[i]
            if result == target:
                count += 1
            return 
        
        for 부호 in [1, -1]:
            arr.append(부호)    
            backtracking()
            arr.pop()
            
    
    backtracking()
    return count