def solution(word):
    arr = []
    
    count = 0
    def dfs():
        nonlocal count
        if "".join(arr) == word:
            return True
        if len(arr) == 5:
            return None
        
        for alpha in 'AEIOU':
            
            arr.append(alpha)
            count += 1
            if dfs() is not None:
                return count 
            arr.pop()
        return None
    return dfs()