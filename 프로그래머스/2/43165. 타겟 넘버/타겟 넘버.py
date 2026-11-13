def solution(numbers, target):
    n = len(numbers)
    
    count = 0
    def dfs(index, num):
        nonlocal count
        if index == n:
            if target == num :
                count += 1
                # print(num)
            return 
        

        dfs(index + 1, num + numbers[index])
        dfs(index + 1, num - numbers[index])
    dfs(0, 0)
    return count