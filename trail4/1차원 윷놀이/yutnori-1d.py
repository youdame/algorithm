n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

answer = -1e9
group_sums = [1] * (k + 1)
def backtrack(depth):
    
    global answer

    if depth == n:
        pass_node = 0
        for p in range(1, k+1):
            group_sum = group_sums[p]
            if group_sum >= m:
                pass_node += 1
        answer = max(answer, pass_node)
                
        return 
    for i in range(1, k+1):
        group_sums[i] += nums[depth]
        
        backtrack(depth + 1)
        group_sums[i] -= nums[depth]


backtrack(0)
print(answer)