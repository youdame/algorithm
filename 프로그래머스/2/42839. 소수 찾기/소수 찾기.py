def is_소수(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
    
def solution(numbers):
    n = len(numbers)
    arr = []
    visited = [False] * len(numbers)
    
    answer = set()
    def dfs():
        if len(arr) > 0:
            new_num = int(''.join(arr))
            print(new_num)
            if is_소수(new_num):
                answer.add(new_num)
 

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                arr.append(numbers[i])
                dfs()
                arr.pop()
                visited[i] = False
    dfs()
            
    return len(answer)
    