n = int(input())
num = list(map(int, input().split()))

# Please write your code here.


total_sum = sum(num)

visited = [False] * (2 * n)

answer = float("inf")
def backtrack(count, sum, idx):
    global answer
    if count == n: 
        # print(visited, sum)
        answer = min(answer, abs((total_sum - sum) - sum))
        return 

    for i in range(idx, 2*n):
        if not visited[i]:
            visited[i] = True
            backtrack(count + 1, sum + num[i], i)
            visited[i] = False

backtrack(0, 0, 0)

print(answer)

