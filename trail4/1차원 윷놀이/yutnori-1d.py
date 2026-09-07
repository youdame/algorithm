n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.


result = []

from collections import defaultdict




answer = -1e9
def backtrack():
    group_sums = [1] * (k + 1)
    global result, answer
    if len(result) == n:
        # print(result)
        for j in range(n):
            group_sums[result[j]] += nums[j]
        pass_node = 0
        for p in range(k+1):
            group_sum = group_sums[p]
            if group_sum >= m:
                pass_node += 1
        # print(result, record, pass_node)
        answer = max(answer, pass_node)
                
        return 
    for i in range(1, k+1):
        result.append(i)
        backtrack()
        result.pop()


backtrack()
print(answer)